# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_GuessDoor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(678, 399)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        Dialog.setFont(font)
        self.startbtn = QtWidgets.QPushButton(Dialog)
        self.startbtn.setGeometry(QtCore.QRect(150, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startbtn.setFont(font)
        self.startbtn.setObjectName("startbtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nb = QtWidgets.QComboBox(Dialog)
        self.nb.setGeometry(QtCore.QRect(60, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nb.setFont(font)
        self.nb.setMaxCount(2147483647)
        self.nb.setObjectName("nb")
        self.nb.addItem("")
        self.nb.addItem("")
        self.nb.addItem("")
        self.nb.addItem("")
        self.nb.addItem("")
        self.btnConfirm = QtWidgets.QPushButton(Dialog)
        self.btnConfirm.setGeometry(QtCore.QRect(150, 110, 91, 171))
        self.btnConfirm.setObjectName("btnConfirm")
        self.tableWidget_result = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_result.setGeometry(QtCore.QRect(250, 0, 401, 351))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.tableWidget_result.setFont(font)
        self.tableWidget_result.setToolTipDuration(-1)
        self.tableWidget_result.setLineWidth(0)
        self.tableWidget_result.setAutoScrollMargin(16)
        self.tableWidget_result.setColumnCount(4)
        self.tableWidget_result.setObjectName("tableWidget_result")
        self.tableWidget_result.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(3, item)
        self.tableWidget_result.horizontalHeader().setDefaultSectionSize(100)
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setGeometry(QtCore.QRect(300, 360, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 50, 131, 301))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_door1 = QtWidgets.QPushButton(self.groupBox)
        self.btn_door1.setGeometry(QtCore.QRect(20, 20, 101, 51))
        self.btn_door1.setObjectName("btn_door1")
        self.btn_door2 = QtWidgets.QPushButton(self.groupBox)
        self.btn_door2.setGeometry(QtCore.QRect(20, 120, 101, 51))
        self.btn_door2.setObjectName("btn_door2")
        self.btn_door3 = QtWidgets.QPushButton(self.groupBox)
        self.btn_door3.setGeometry(QtCore.QRect(20, 210, 101, 51))
        self.btn_door3.setObjectName("btn_door3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 360, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.startbtn.setText(_translate("Dialog", "开始"))
        self.label.setText(_translate("Dialog", "局数："))
        self.nb.setItemText(0, _translate("Dialog", "0"))
        self.nb.setItemText(1, _translate("Dialog", "5"))
        self.nb.setItemText(2, _translate("Dialog", "10"))
        self.nb.setItemText(3, _translate("Dialog", "15"))
        self.nb.setItemText(4, _translate("Dialog", "20"))
        self.btnConfirm.setText(_translate("Dialog", "选\n"
"定"))
        item = self.tableWidget_result.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "局数"))
        item = self.tableWidget_result.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "目标门号"))
        item = self.tableWidget_result.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "最终门号"))
        item = self.tableWidget_result.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "是否中奖"))
        self.label_result.setText(_translate("Dialog", "0"))
        self.btn_door1.setText(_translate("Dialog", "门1"))
        self.btn_door2.setText(_translate("Dialog", "门2"))
        self.btn_door3.setText(_translate("Dialog", "门3"))
        self.label_2.setText(_translate("Dialog", "概率："))

