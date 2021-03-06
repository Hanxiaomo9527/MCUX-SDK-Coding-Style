# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MCUX-SDK-CodingStyleChecker.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_codingStyleSetting = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_codingStyleSetting.setGeometry(QtCore.QRect(10, 10, 81, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.pushButton_codingStyleSetting.setFont(font)
        self.pushButton_codingStyleSetting.setObjectName("pushButton_codingStyleSetting")
        self.textEdit_log = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_log.setGeometry(QtCore.QRect(10, 90, 621, 411))
        self.textEdit_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_log.setObjectName("textEdit_log")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 510, 711, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textEdit_fileFolderFilter = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_fileFolderFilter.setGeometry(QtCore.QRect(190, 60, 441, 21))
        self.textEdit_fileFolderFilter.setObjectName("textEdit_fileFolderFilter")
        self.label_fileFolderFilter = QtWidgets.QLabel(self.centralwidget)
        self.label_fileFolderFilter.setGeometry(QtCore.QRect(100, 50, 91, 31))
        self.label_fileFolderFilter.setObjectName("label_fileFolderFilter")
        self.textEdit_inputFileFolder = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_inputFileFolder.setGeometry(QtCore.QRect(190, 10, 371, 41))
        self.textEdit_inputFileFolder.setObjectName("textEdit_inputFileFolder")
        self.label_selectFileFolder = QtWidgets.QLabel(self.centralwidget)
        self.label_selectFileFolder.setGeometry(QtCore.QRect(100, 10, 91, 31))
        self.label_selectFileFolder.setObjectName("label_selectFileFolder")
        self.pushButton_browseFileFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browseFileFolder.setGeometry(QtCore.QRect(640, 10, 81, 31))
        self.pushButton_browseFileFolder.setObjectName("pushButton_browseFileFolder")
        self.checkBox_isFolder = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_isFolder.setGeometry(QtCore.QRect(570, 10, 61, 31))
        self.checkBox_isFolder.setObjectName("checkBox_isFolder")
        self.pushButton_doCheck = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_doCheck.setGeometry(QtCore.QRect(640, 50, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_doCheck.setFont(font)
        self.pushButton_doCheck.setObjectName("pushButton_doCheck")
        self.pushButton_saveLog = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_saveLog.setGeometry(QtCore.QRect(640, 470, 81, 31))
        self.pushButton_saveLog.setObjectName("pushButton_saveLog")
        self.label_errorRate = QtWidgets.QLabel(self.centralwidget)
        self.label_errorRate.setGeometry(QtCore.QRect(640, 110, 71, 31))
        self.label_errorRate.setObjectName("label_errorRate")
        self.lcdNumber_errorRate = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_errorRate.setGeometry(QtCore.QRect(640, 140, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber_errorRate.setFont(font)
        self.lcdNumber_errorRate.setLineWidth(3)
        self.lcdNumber_errorRate.setMidLineWidth(1)
        self.lcdNumber_errorRate.setDigitCount(4)
        self.lcdNumber_errorRate.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_errorRate.setProperty("value", 100.0)
        self.lcdNumber_errorRate.setProperty("intValue", 100)
        self.lcdNumber_errorRate.setObjectName("lcdNumber_errorRate")
        self.label_totalErrorLines = QtWidgets.QLabel(self.centralwidget)
        self.label_totalErrorLines.setGeometry(QtCore.QRect(640, 200, 81, 31))
        self.label_totalErrorLines.setObjectName("label_totalErrorLines")
        self.label_totalCodeLines = QtWidgets.QLabel(self.centralwidget)
        self.label_totalCodeLines.setGeometry(QtCore.QRect(640, 270, 81, 31))
        self.label_totalCodeLines.setObjectName("label_totalCodeLines")
        self.lineEdit_totalCodeLines = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_totalCodeLines.setGeometry(QtCore.QRect(640, 300, 81, 31))
        self.lineEdit_totalCodeLines.setText("")
        self.lineEdit_totalCodeLines.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_totalCodeLines.setReadOnly(True)
        self.lineEdit_totalCodeLines.setObjectName("lineEdit_totalCodeLines")
        self.lineEdit_totalErrorLines = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_totalErrorLines.setGeometry(QtCore.QRect(640, 230, 81, 31))
        self.lineEdit_totalErrorLines.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_totalErrorLines.setReadOnly(True)
        self.lineEdit_totalErrorLines.setObjectName("lineEdit_totalErrorLines")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMenuHelpHomePage = QtWidgets.QAction(MainWindow)
        self.actionMenuHelpHomePage.setAutoRepeat(True)
        self.actionMenuHelpHomePage.setObjectName("actionMenuHelpHomePage")
        self.actionMenuHelpAboutAuthor = QtWidgets.QAction(MainWindow)
        self.actionMenuHelpAboutAuthor.setObjectName("actionMenuHelpAboutAuthor")
        self.actionMenuHelpRevisionHistory = QtWidgets.QAction(MainWindow)
        self.actionMenuHelpRevisionHistory.setObjectName("actionMenuHelpRevisionHistory")
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionMenuHelpHomePage)
        self.menuHelp.addAction(self.actionMenuHelpAboutAuthor)
        self.menuHelp.addAction(self.actionMenuHelpRevisionHistory)
        self.menuHelp.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MCUXpresso SDK Coding Style Checker"))
        self.pushButton_codingStyleSetting.setText(_translate("MainWindow", "Coding Style \n"
" Setting"))
        self.label_fileFolderFilter.setText(_translate("MainWindow", "File/Folder Filter:"))
        self.label_selectFileFolder.setText(_translate("MainWindow", "Select File/Folder:"))
        self.pushButton_browseFileFolder.setText(_translate("MainWindow", "Browse"))
        self.checkBox_isFolder.setText(_translate("MainWindow", "Is Folder"))
        self.pushButton_doCheck.setText(_translate("MainWindow", "Check"))
        self.pushButton_saveLog.setText(_translate("MainWindow", "Save Log"))
        self.label_errorRate.setText(_translate("MainWindow", "Error Rate (%)"))
        self.label_totalErrorLines.setText(_translate("MainWindow", "Total Error Lines"))
        self.label_totalCodeLines.setText(_translate("MainWindow", "Total Code Lines"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionMenuHelpHomePage.setText(_translate("MainWindow", "Home Page"))
        self.actionMenuHelpAboutAuthor.setText(_translate("MainWindow", "About Author"))
        self.actionMenuHelpRevisionHistory.setText(_translate("MainWindow", "Revision History"))

