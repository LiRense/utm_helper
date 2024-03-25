# This Python file uses the following encoding: utf-8
import sys
import platform
import os
import re
#from subprocess import PIPE, Popen
#import getpass
import subprocess
from datetime import datetime,timezone
import time

import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QApplication, QMainWindow,QFileDialog, QDialog,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QMessageBox,QCheckBox)
from PySide6 import QtCore
from PySide6.QtCore import (Qt, QSize)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import *
import requests
import json

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.progressBar.hide()
        self.ui.textEdit.setEnabled(True)
        self.ui.textEdit.setReadOnly(True)

        self.check_password()
        self.get_os()
        self.get_utm_data()
        self.check_installed()


        self.ui.install_bt.clicked.connect(self.install_click)
        self.ui.dalete_bt.clicked.connect(self.delete_click)

    def get_os(self):
        os_data = platform.system()
        if os_data == 'Linux':
            self.directory_path = '/opt/utm/'
        elif os_data == 'Windows':
            self.directory_path = 'C:/UTM/'
        self.ui.label.setText('OS: '+ os_data)

    def get_version_UTM_Linux(self):
        os.system(f'echo {self.password} | sudo -S chown -R ivan:root /opt/')
        with open(self.directory_path + 'transport/l/transport_info.log') as logs:
            pass


    def turn_buttons_on(self):
        self.ui.install_bt.setEnabled(False)

        self.ui.activation_key.setEnabled(True)
        self.ui.dalete_bt.setEnabled(True)
        self.ui.start_bt.setEnabled(True)
        self.ui.stop_bt.setEnabled(True)
        self.ui.restart_bt.setEnabled(True)
        self.ui.clear_bt.setEnabled(True)
        self.ui.shifr_bt.setEnabled(True)
        self.ui.templates_bt.setEnabled(True)

    def turn_buttons_off(self):
        self.ui.install_bt.setEnabled(True)
        self.ui.activation_key.setEnabled(True)

        self.ui.dalete_bt.setEnabled(False)
        self.ui.start_bt.setEnabled(False)
        self.ui.stop_bt.setEnabled(False)
        self.ui.restart_bt.setEnabled(False)
        self.ui.clear_bt.setEnabled(False)
        self.ui.shifr_bt.setEnabled(False)
        self.ui.templates_bt.setEnabled(False)

    def get_utm_data(self):
        self.version = 'Версия УТМ: '
        countur = 'Контур: '
        status_data = 'Статус настроек: '
        key_data = 'Ключ: '
        try:
            headers = {'Accept': 'application/json'}
            response = requests.get('http://localhost:8080/api/info/list',headers=headers)
            data = response.json()
            self.ui.version.setText(self.version+data['version'])
            self.ui.contur_data.setText(countur+data['contour'])
            self.ui.key_data.setText(status_data)
            self.ui.status_data.setText(key_data)

            self.turn_buttons_on()


        except requests.exceptions.ConnectionError:
            self.version = 'Версия УТМ: не установлена'
            self.ui.version.setText(self.version)
            self.ui.contur_data.setText(countur)
            self.ui.key_data.setText(key_data)
            self.ui.status_data.setText(status_data)

            self.turn_buttons_off()

    def clear_logs(self):
        command = 'echo {self.password} | sudo -S rm /opt/utm/transport/l/transport_info.log'
        command2 = 'echo {self.password} | sudo chown -R ivan:root /opt/utm'
        try:
            output = subprocess.check_output(command, shell=True, text=True)
            output2 = subprocess.check_output(command2, shell=True, text=True)
        except:
            pass

    def progressbar_use(self,status=None, counter=0):
        if status == None:
            self.ui.progressBar.setValue(counter)
        elif status == 'start':
            bar_complited = 0
            self.ui.progressBar.setValue(bar_complited)
            self.ui.progressBar.setVisible(True)
        elif status == 'end':
            bar_complited = 0
            self.ui.progressBar.setValue(bar_complited)
            self.ui.progressBar.setVisible(False)


    def install_click(self):
        while self.password_status == 'bad':
            self.dialog_autorisation()
        utc_cur_date = datetime.now(timezone.utc)
        dialog = QFileDialog(self)
        url = dialog.getOpenFileUrl(None,caption="Выберите пакет для установки",filter=("u-trans-*.deb"))[0].path()

        command = f'echo {self.password} | sudo -S  dpkg --install {url}'

        self.progressbar_use(status='start', counter=50)

        output = subprocess.check_output(command, shell=True, text=True)
        self.ui.textEdit.append(str(output))
        self.ui.textEdit.append(str(utc_cur_date)+' | УТМ установлена')

        self.progressbar_use(status='end')

        self.get_os()
        self.get_utm_data()

    def sudo_checker(self):
        try:
            command = f'echo {self.password} | sudo -S -v'
            output = subprocess.check_output(command, shell=True, text=True)
            self.password_status = 'ok'
        except subprocess.CalledProcessError:
            self.password_status = 'bad'

    def check_installed(self):
        if os.path.exists('/opt/utm') and self.version == 'Версия УТМ: не установлена':
            self.turn_buttons_off()
            self.ui.install_bt.setEnabled(False)
            self.ui.dalete_bt.setEnabled(True)




    def check_password(self):
        self.password = ''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if os.path.exists(dir_path+'/bin'):
            with open(dir_path+'/bin/config','r') as file:
                lines = file.readlines()
                for i in lines:
                    if 'password: ' in i:
                        self.password = re.sub('password: ','',i)
                        self.sudo_checker()
                        return
                    else:
                        self.password_status = 'bad'
        self.password_status = 'bad'



    def delete_click(self):
        while self.password_status == 'bad':
            self.dialog_autorisation()
        utc_cur_date = datetime.now(timezone.utc)
        dat = (str(utc_cur_date)[0:19])
        dat = dat.replace(" ","_")
        dat = dat.replace(":", "-")
        if not os.path.exists('dumbsDB'):
            os.mkdir('dumbsDB')
        spis = [f'echo {self.password} | sudo -S cp -r /opt/utm/transport/transportDB dumbsDB/transportDB_{dat}',
                f"echo {self.password} | sudo -S dpkg --purge u-trans",
                f'echo {self.password} | sudo -S rm -r /opt/utm/',
                f'echo {self.password} | sudo -S rm -r /opt/utm/']
        self.progressbar_use(status='start')
        i=0
        for i in spis:
            i += 25
            try:
                output = subprocess.check_output(i, shell=True, text=True)
                self.ui.textEdit.append(str(output))
                self.progressbar_use(counter=i)
            except:
                self.progressbar_use(counter=i)
#        filen = open('save_conf/last_prop.txt','w')
#        filen.close()
        self.progressbar_use(status='end')
        self.ui.textEdit.setPlainText(str(utc_cur_date)+' | УТМ удалена с вашего ПК')
        self.ui.textEdit.append(str(utc_cur_date)+' | БД документов сохранена')
        self.get_os()
        self.get_utm_data()



    def dialog_autorisation(self):
        dialog = QDialog(self)

        ql = QLineEdit()
        ql.setEchoMode(QLineEdit.Password)
        l = QLabel('Введите пароль для доступа приложения к вашим файлам')
        ok_bt = QPushButton('Accept')
        cancel = QPushButton('Cancel')

        cheq = QCheckBox('Сохранять пароль?')

        layV = QVBoxLayout()
        layH = QHBoxLayout()

        layH.addWidget(ok_bt)
        layH.addWidget(cancel)

        layV.addWidget(l)
        layV.addWidget(ql)
        layV.addWidget(cheq)
        layV.addLayout(layH)

        dialog.setLayout(layV)

        cancel.clicked.connect(dialog.close)
        ok_bt.clicked.connect(dialog.accept)

        if dialog.exec():
            self.password = ql.text()
            if cheq.isEnabled():
                if not os.path.exists('bin'):
                    os.mkdir('bin')
                file = open('bin/config','w')
                file.write('password: '+self.password)
            self.sudo_checker()
        else:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setFixedSize(513,636)
    widget.show()
    sys.exit(app.exec())
