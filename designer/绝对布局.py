# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '绝对布局.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 60, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 40, 111, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 170, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(210, 170, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(50, 290, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(190, 290, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 340, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(350, 290, 431, 241))
        self.webEngineView.setUrl(QtCore.QUrl("https://www.baidu.com/"))
        self.webEngineView.setObjectName("webEngineView")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(350, 10, 431, 261))
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))

from PyQt5 import QtWebEngineWidgets
