#coding=gbk
import sys
import random
'''from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox'''
from ui_GuessDoor import Ui_Dialog
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.startbtn.clicked.connect(self.start)
        self.ui.btn_door1.clicked.connect(self.door1)
        self.ui.btn_door2.clicked.connect(self.door2)
        self.ui.btn_door3.clicked.connect(self.door3)
        self.ui.btnConfirm.clicked.connect(self.confirm)
        # ���������ţ����涼����(���ڵ�һ��ɾ����
        self.three_door = ['Door1', 'Door2', 'Door3']
        # ���������ţ����涼���򣨵���ʶ����ѡ�ţ�
        self.three_door1 = ['Door1', 'Door2', 'Door3']
        #��һ��ѡ
        self.choose_door = ''
        #�ڶ���ѡ
        self.rother_door = ''
        #��������
        self.number = 0
        self.number1 = 0
        self.chance = 0
        #ͳ�Ʊ�
        self.table()
        self.nm = -1
        self.firstdoor = ''
        self.finaldoor = ''
        self.end = ''




        '''newItem = self.ui.QtableWidget_result.horizontalHeaderItem(1)
        self.ui.tableWidget_result.setItem(0, 0, self.newItem)

        newItem =  self.ui.QtableWidget_result.horizontalHeaderItem(1)
        self.ui.tableWidget_result.setItem(0, 1, newItem)

        newItem =  self.ui.QtableWidget_result.horizontalHeaderItem(1)
        self.ui.tableWidget_result.setItem(0, 2, newItem)'''

    def table(self):
        self.ui.tableWidget_result.setColumnCount(5)
        self.ui.tableWidget_result.setRowCount(20)
        j = 0 # �ڼ��У���0��ʼ��
        i = 0#�ڼ��У���0��ʼ��
        Value = '1'#����
        self.ui.tableWidget_result.setItem(j, i, QTableWidgetItem(Value))#����j��i�е�����ΪValue
        self.ui.tableWidget_result.setColumnWidth(j,50)#����j�еĿ��
        self.ui.tableWidget_result.setRowHeight(i,50)#����i�еĸ߶�
        self.ui.tableWidget_result.verticalHeader().setVisible(False)
        


    def start(self):
        self.number = int(self.ui.nb.currentText())
        # �����һ���ź���򻻳ɳ�
        a = random.choice(self.three_door)
        if a == 'Door1':
            self.three_door[0] = 'car'
            self.three_door1[0] = 'car'
        if a == 'Door2':
            self.three_door[1] = 'car'
            self.three_door1[1] = 'car'
        if a == 'Door3':
            self.three_door[2] = 'car'
            self.three_door1[2] = 'car'
        print(self.three_door)
        print(self.three_door1)
    def door1(self):
        #��һ��ѡ����1
        self.choose_door = self.three_door1[0]

    def door2(self):
        # ��һ��ѡ����2
        self.choose_door = self.three_door1[1]

    def door3(self):
        # ��һ��ѡ����3
        self.choose_door = self.three_door1[2]

    def confirm(self):
        if len(self.rother_door) != 1:
            self.firstdoor = self.choose_door
            self.rother_door = self.three_door
            # �������������к������һ����
            for door in self.rother_door:
                if door == 'car':
                    self.rother_door.remove(door)
            for door in self.rother_door:
                if door != self.choose_door and door == 'Door1':
                    self.rother_door.remove(door)
                    self.ui.btn_door1.setVisible(False)
                    break
                if door != self.choose_door and door == 'Door2':
                    self.rother_door.remove(door)
                    self.ui.btn_door2.setVisible(False)
                    break
                if door != self.choose_door and door == 'Door3':
                    self.rother_door.remove(door)
                    self.ui.btn_door3.setVisible(False)
                    break
                print(self.rother_door)
        else:
            self.finaldoor = self.choose_door
            if self.choose_door == 'car':
                reply = QMessageBox.warning(self, '��Ϣ', '��ϲ����һ����', QMessageBox.Yes, QMessageBox.Yes)
                self.end = '��'
                self.chance = self.chance + 1

            else:
                reply = QMessageBox.warning(self, '��Ϣ', '���ź�����δ���г�', QMessageBox.Yes, QMessageBox.Yes)
                self.end = '��'
            self.number1 = self.number1 + 1
            self.ui.btn_door1.setVisible(True)
            self.ui.btn_door2.setVisible(True)
            self.ui.btn_door3.setVisible(True)
            self.nm = self.nm + 1
            self.rother_door = ''
            self.ui.tableWidget_result.setItem(self.nm , 0, QTableWidgetItem(str(self.nm+1)))
            self.ui.tableWidget_result.setItem(self.nm , 1, QTableWidgetItem(self.firstdoor))
            self.ui.tableWidget_result.setItem(self.nm , 2, QTableWidgetItem(self.finaldoor))
            self.ui.tableWidget_result.setItem(self.nm , 3, QTableWidgetItem(self.end))
            self.three_door = ['Door1', 'Door2', 'Door3']
            self.three_door1 = ['Door1', 'Door2', 'Door3']
            a = random.choice(self.three_door)
            if a == 'Door1':
                self.three_door[0] = 'car'
                self.three_door1[0] = 'car'
            if a == 'Door2':
                self.three_door[1] = 'car'
                self.three_door1[1] = 'car'
            if a == 'Door3':
                self.three_door[2] = 'car'
                self.three_door1[2] = 'car'
            if self.number1 == self.number:
                reply = QMessageBox.warning(self, '��Ϣ', '��Ϸ����', QMessageBox.Yes, QMessageBox.Yes)
                self.ui.label_result.setText(str('%.1f' %((self.chance/int(self.number))*100))+"%")



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())