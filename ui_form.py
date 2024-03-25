# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(513, 636)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.gridLayout_2.addWidget(self.progressBar, 6, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stop_bt = QPushButton(self.groupBox_4)
        self.stop_bt.setObjectName(u"stop_bt")

        self.gridLayout_3.addWidget(self.stop_bt, 0, 0, 1, 1)

        self.start_bt = QPushButton(self.groupBox_4)
        self.start_bt.setObjectName(u"start_bt")

        self.gridLayout_3.addWidget(self.start_bt, 0, 1, 1, 1)

        self.restart_bt = QPushButton(self.groupBox_4)
        self.restart_bt.setObjectName(u"restart_bt")

        self.gridLayout_3.addWidget(self.restart_bt, 1, 0, 1, 1)

        self.clear_bt = QPushButton(self.groupBox_4)
        self.clear_bt.setObjectName(u"clear_bt")

        self.gridLayout_3.addWidget(self.clear_bt, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dalete_bt = QPushButton(self.groupBox)
        self.dalete_bt.setObjectName(u"dalete_bt")

        self.gridLayout.addWidget(self.dalete_bt, 1, 0, 1, 1)

        self.install_bt = QPushButton(self.groupBox)
        self.install_bt.setObjectName(u"install_bt")

        self.gridLayout.addWidget(self.install_bt, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout = QFormLayout(self.groupBox_5)
        self.formLayout.setObjectName(u"formLayout")
        self.version = QLabel(self.groupBox_5)
        self.version.setObjectName(u"version")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.version)

        self.contur_data = QLabel(self.groupBox_5)
        self.contur_data.setObjectName(u"contur_data")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.contur_data)

        self.key_data = QLabel(self.groupBox_5)
        self.key_data.setObjectName(u"key_data")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.key_data)

        self.status_data = QLabel(self.groupBox_5)
        self.status_data.setObjectName(u"status_data")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.status_data)

        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)


        self.gridLayout_2.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)

        self.gridLayout_2.addWidget(self.textEdit, 5, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.templates_bt = QPushButton(self.groupBox_3)
        self.templates_bt.setObjectName(u"templates_bt")

        self.gridLayout_4.addWidget(self.templates_bt, 0, 1, 1, 1)

        self.shifr_bt = QPushButton(self.groupBox_3)
        self.shifr_bt.setObjectName(u"shifr_bt")

        self.gridLayout_4.addWidget(self.shifr_bt, 0, 0, 1, 1)

        self.activation_key = QPushButton(self.groupBox_3)
        self.activation_key.setObjectName(u"activation_key")

        self.gridLayout_4.addWidget(self.activation_key, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 4, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("mainWindow", u"\u0411\u044b\u0441\u0442\u0440\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.stop_bt.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0423\u0422\u041c", None))
        self.start_bt.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \u0423\u0422\u041c", None))
        self.restart_bt.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u043a \u0423\u0422\u041c", None))
        self.clear_bt.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0447\u0438\u0441\u0442\u043a\u0430 \u0411\u0414", None))
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435/\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430", None))
        self.dalete_bt.setText(QCoreApplication.translate("mainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0423\u0422\u041c", None))
        self.install_bt.setText(QCoreApplication.translate("mainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0423\u0422\u041c", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("mainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.version.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f \u0423\u0422\u041c: ", None))
        self.contur_data.setText(QCoreApplication.translate("mainWindow", u"\u041a\u043e\u043d\u0442\u0443\u0440:", None))
        self.key_data.setText(QCoreApplication.translate("mainWindow", u"\u041a\u043b\u044e\u0447:", None))
        self.status_data.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a:", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"OS: ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043a\u043b\u044e\u0447\u0430", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.templates_bt.setText(QCoreApplication.translate("mainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a", None))
        self.shifr_bt.setText(QCoreApplication.translate("mainWindow", u"\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.activation_key.setText(QCoreApplication.translate("mainWindow", u"\u0410\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u044f \u043a\u043b\u044e\u0447\u0435\u0439", None))
    # retranslateUi

