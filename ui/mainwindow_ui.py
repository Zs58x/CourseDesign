# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 860)
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 141, 751))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 121, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_loadimg = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_loadimg.setObjectName("btn_loadimg")
        self.verticalLayout.addWidget(self.btn_loadimg)
        self.btn_loadvideo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_loadvideo.setObjectName("btn_loadvideo")
        self.verticalLayout.addWidget(self.btn_loadvideo)
        self.btn_opencamera = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_opencamera.setObjectName("btn_opencamera")
        self.verticalLayout.addWidget(self.btn_opencamera)
        self.btn_initweight = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_initweight.setObjectName("btn_initweight")
        self.verticalLayout.addWidget(self.btn_initweight)
        self.btn_closecamera = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_closecamera.setObjectName("btn_closecamera")
        self.verticalLayout.addWidget(self.btn_closecamera)
        self.btn_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_clear.setObjectName("btn_clear")
        self.verticalLayout.addWidget(self.btn_clear)
        self.btn_going = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_going.setObjectName("btn_going")
        self.verticalLayout.addWidget(self.btn_going)
        self.btn_stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_stop.setObjectName("btn_stop")
        self.verticalLayout.addWidget(self.btn_stop)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(170, 50, 1181, 591))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_origin = QtWidgets.QLabel(self.groupBox_2)
        self.label_origin.setGeometry(QtCore.QRect(10, 30, 571, 551))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(15)
        self.label_origin.setFont(font)
        self.label_origin.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_origin.setObjectName("label_origin")
        self.label_detect = QtWidgets.QLabel(self.groupBox_2)
        self.label_detect.setGeometry(QtCore.QRect(600, 30, 571, 551))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(15)
        self.label_detect.setFont(font)
        self.label_detect.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.label_detect.setAlignment(QtCore.Qt.AlignCenter)
        self.label_detect.setObjectName("label_detect")
        self.label_mian_titlle = QtWidgets.QLabel(self.centralwidget)
        self.label_mian_titlle.setGeometry(QtCore.QRect(530, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        self.label_mian_titlle.setFont(font)
        self.label_mian_titlle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_mian_titlle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mian_titlle.setObjectName("label_mian_titlle")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1040, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        self.lcdNumber.setFont(font)
        self.lcdNumber.setDigitCount(19)
        self.lcdNumber.setObjectName("lcdNumber")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(170, 650, 581, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser_print = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_print.setGeometry(QtCore.QRect(10, 20, 561, 141))
        self.textBrowser_print.setObjectName("textBrowser_print")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(770, 650, 581, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textBrowser_detect = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser_detect.setGeometry(QtCore.QRect(10, 20, 561, 141))
        self.textBrowser_detect.setObjectName("textBrowser_detect")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "火焰监测"))
        self.groupBox.setTitle(_translate("MainWindow", "操作区"))
        self.btn_loadimg.setText(_translate("MainWindow", "图片检测"))
        self.btn_loadvideo.setText(_translate("MainWindow", "视频检测"))
        self.btn_opencamera.setText(_translate("MainWindow", "打开摄像头"))
        self.btn_initweight.setText(_translate("MainWindow", "摄像头检测"))
        self.btn_closecamera.setText(_translate("MainWindow", "关闭摄像头"))
        self.btn_clear.setText(_translate("MainWindow", "清除"))
        self.btn_going.setText(_translate("MainWindow", "暂停"))
        self.btn_stop.setText(_translate("MainWindow", "停止视频播放"))
        self.groupBox_2.setTitle(_translate("MainWindow", "显示区域"))
        self.label_origin.setText(_translate("MainWindow", "原图区域"))
        self.label_detect.setText(_translate("MainWindow", "检测区域"))
        self.label_mian_titlle.setText(_translate("MainWindow", "火焰监测系统"))
        self.groupBox_3.setTitle(_translate("MainWindow", "打印输出"))
        self.groupBox_4.setTitle(_translate("MainWindow", "检测输出"))