# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/mainwindow.ui',
# licensing of 'designer/mainwindow.ui' applies.
#
# Created: Mon May 20 16:11:39 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1269, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.tempA_LCD = QtWidgets.QLCDNumber(self.groupBox)
        self.tempA_LCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tempA_LCD.setSmallDecimalPoint(False)
        self.tempA_LCD.setObjectName("tempA_LCD")
        self.gridLayout_2.addWidget(self.tempA_LCD, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.tempC_LCD = QtWidgets.QLCDNumber(self.groupBox)
        self.tempC_LCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tempC_LCD.setObjectName("tempC_LCD")
        self.gridLayout_2.addWidget(self.tempC_LCD, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.tempB_LCD = QtWidgets.QLCDNumber(self.groupBox)
        self.tempB_LCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tempB_LCD.setObjectName("tempB_LCD")
        self.gridLayout_2.addWidget(self.tempB_LCD, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_16 = QtWidgets.QLabel(self.groupBox_6)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 3, 0, 1, 1)
        self.CHX_VDD = QtWidgets.QLCDNumber(self.groupBox_6)
        self.CHX_VDD.setMinimumSize(QtCore.QSize(0, 32))
        self.CHX_VDD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHX_VDD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHX_VDD.setObjectName("CHX_VDD")
        self.gridLayout_7.addWidget(self.CHX_VDD, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_6)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)
        self.CHX_M = QtWidgets.QLCDNumber(self.groupBox_6)
        self.CHX_M.setMinimumSize(QtCore.QSize(0, 32))
        self.CHX_M.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHX_M.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHX_M.setObjectName("CHX_M")
        self.gridLayout_7.addWidget(self.CHX_M, 2, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 0, 2, 1, 1)
        self.CHX_BIAS = QtWidgets.QLCDNumber(self.groupBox_6)
        self.CHX_BIAS.setMinimumSize(QtCore.QSize(0, 32))
        self.CHX_BIAS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHX_BIAS.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHX_BIAS.setObjectName("CHX_BIAS")
        self.gridLayout_7.addWidget(self.CHX_BIAS, 3, 1, 1, 1)
        self.CHX_PW_I = QtWidgets.QLCDNumber(self.groupBox_6)
        self.CHX_PW_I.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHX_PW_I.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHX_PW_I.setObjectName("CHX_PW_I")
        self.gridLayout_7.addWidget(self.CHX_PW_I, 0, 3, 1, 1)
        self.CHX_PW_V = QtWidgets.QLCDNumber(self.groupBox_6)
        self.CHX_PW_V.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.CHX_PW_V.setFont(font)
        self.CHX_PW_V.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHX_PW_V.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHX_PW_V.setObjectName("CHX_PW_V")
        self.gridLayout_7.addWidget(self.CHX_PW_V, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 0, 4, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 1, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 2, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_7.addWidget(self.label_27, 3, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.CHY_PW_V = QtWidgets.QLCDNumber(self.groupBox_5)
        self.CHY_PW_V.setMinimumSize(QtCore.QSize(0, 32))
        self.CHY_PW_V.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHY_PW_V.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHY_PW_V.setObjectName("CHY_PW_V")
        self.gridLayout_6.addWidget(self.CHY_PW_V, 0, 1, 1, 1)
        self.CHY_PW_I = QtWidgets.QLCDNumber(self.groupBox_5)
        self.CHY_PW_I.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHY_PW_I.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHY_PW_I.setObjectName("CHY_PW_I")
        self.gridLayout_6.addWidget(self.CHY_PW_I, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)
        self.CHY_BIAS = QtWidgets.QLCDNumber(self.groupBox_5)
        self.CHY_BIAS.setMinimumSize(QtCore.QSize(0, 32))
        self.CHY_BIAS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHY_BIAS.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHY_BIAS.setObjectName("CHY_BIAS")
        self.gridLayout_6.addWidget(self.CHY_BIAS, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)
        self.CHY_M = QtWidgets.QLCDNumber(self.groupBox_5)
        self.CHY_M.setMinimumSize(QtCore.QSize(0, 32))
        self.CHY_M.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHY_M.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHY_M.setObjectName("CHY_M")
        self.gridLayout_6.addWidget(self.CHY_M, 2, 1, 1, 1)
        self.CHY_VDD = QtWidgets.QLCDNumber(self.groupBox_5)
        self.CHY_VDD.setMinimumSize(QtCore.QSize(0, 32))
        self.CHY_VDD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHY_VDD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHY_VDD.setObjectName("CHY_VDD")
        self.gridLayout_6.addWidget(self.CHY_VDD, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 0, 4, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 1, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 2, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_6.addWidget(self.label_33, 3, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 0, 1, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.CHZ_BIAS = QtWidgets.QLCDNumber(self.groupBox_4)
        self.CHZ_BIAS.setMinimumSize(QtCore.QSize(0, 32))
        self.CHZ_BIAS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHZ_BIAS.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHZ_BIAS.setObjectName("CHZ_BIAS")
        self.gridLayout_5.addWidget(self.CHZ_BIAS, 3, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 0, 2, 1, 1)
        self.CHZ_M = QtWidgets.QLCDNumber(self.groupBox_4)
        self.CHZ_M.setMinimumSize(QtCore.QSize(0, 32))
        self.CHZ_M.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHZ_M.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHZ_M.setObjectName("CHZ_M")
        self.gridLayout_5.addWidget(self.CHZ_M, 2, 1, 1, 1)
        self.CHZ_VDD = QtWidgets.QLCDNumber(self.groupBox_4)
        self.CHZ_VDD.setMinimumSize(QtCore.QSize(0, 32))
        self.CHZ_VDD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHZ_VDD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHZ_VDD.setObjectName("CHZ_VDD")
        self.gridLayout_5.addWidget(self.CHZ_VDD, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 1)
        self.CHZ_PW_V = QtWidgets.QLCDNumber(self.groupBox_4)
        self.CHZ_PW_V.setMinimumSize(QtCore.QSize(0, 32))
        self.CHZ_PW_V.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHZ_PW_V.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHZ_PW_V.setObjectName("CHZ_PW_V")
        self.gridLayout_5.addWidget(self.CHZ_PW_V, 0, 1, 1, 1)
        self.CHZ_PW_I = QtWidgets.QLCDNumber(self.groupBox_4)
        self.CHZ_PW_I.setMinimumSize(QtCore.QSize(0, 32))
        self.CHZ_PW_I.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CHZ_PW_I.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.CHZ_PW_I.setObjectName("CHZ_PW_I")
        self.gridLayout_5.addWidget(self.CHZ_PW_I, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 0, 4, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 1, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 2, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 3, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 2, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 3, 3, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Launch_Measurements = QtWidgets.QPushButton(self.groupBox_2)
        self.Launch_Measurements.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.Launch_Measurements.setFont(font)
        self.Launch_Measurements.setObjectName("Launch_Measurements")
        self.gridLayout_3.addWidget(self.Launch_Measurements, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        self.notes_label = QtWidgets.QLabel(self.groupBox_2)
        self.notes_label.setObjectName("notes_label")
        self.gridLayout_3.addWidget(self.notes_label, 0, 0, 1, 1)
        self.power_button = QtWidgets.QPushButton(self.groupBox_2)
        self.power_button.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.power_button.setFont(font)
        self.power_button.setObjectName("power_button")
        self.gridLayout_3.addWidget(self.power_button, 2, 3, 1, 1)
        self.notes = QtWidgets.QTextEdit(self.groupBox_2)
        self.notes.setObjectName("notes")
        self.gridLayout_3.addWidget(self.notes, 0, 1, 1, 3)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1269, 27))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuSettings.addAction(self.actionSettings)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Juice_SCM_GSE", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Temperatures", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Temperature B", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Temperature C", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "°C", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "°C", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "°C", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Temperature A", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Voltages", None, -1))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("MainWindow", "Asic channel X", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("MainWindow", "BIAS", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("MainWindow", "VDD", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("MainWindow", "Power supply", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("MainWindow", "M", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("MainWindow", "mA", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label_27.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "Asic channel Y", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("MainWindow", "VDD", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "M", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "BIAS", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("MainWindow", "Power supply", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("MainWindow", "mA", None, -1))
        self.label_31.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label_32.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label_33.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Asic channel Z", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("MainWindow", "M", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "VDD", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Power supply", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "BIAS", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("MainWindow", "mA", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label_29.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label_30.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Measurements", None, -1))
        self.Launch_Measurements.setText(QtWidgets.QApplication.translate("MainWindow", "Launch measurements", None, -1))
        self.notes_label.setText(QtWidgets.QApplication.translate("MainWindow", "Notes, radiation level...:", None, -1))
        self.power_button.setText(QtWidgets.QApplication.translate("MainWindow", "Turn ON", None, -1))
        self.menuSettings.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))

from . import resources_rc
