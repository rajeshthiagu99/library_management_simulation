# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import platform

if platform.system() == 'Windows':
   abs_path = (("\\").join((os.getcwd()).split("\\")[:-1])).replace('\\','\\\\')
if platform.system() == 'Linux':
   abs_path = ("/").join((os.getcwd()).split("/")[:-1])+"/"
sys.path.insert(0,r'{}'.format(abs_path))

from qrc_files import images_rc



class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(1920, 1080)
        Home.setMaximumSize(QtCore.QSize(1920, 1080))
        Home.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.frame.setMaximumSize(QtCore.QSize(1920, 1080))
        self.frame.setStyleSheet("background-image: url(:/bg_images/bg_main.png);\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.welcome_label = QtWidgets.QLabel(self.frame)
        self.welcome_label.setGeometry(QtCore.QRect(560, 10, 741, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("QLabel{\n"
"color: rgb(105, 157, 238);\n"
"background: rgba( 4, 7, 15, 0 );\n"
"}\n"
"")
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setWordWrap(True)
        self.welcome_label.setObjectName("welcome_label")
        self.borrow_book_button = QtWidgets.QPushButton(self.frame)
        self.borrow_book_button.setGeometry(QtCore.QRect(370, 160, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.borrow_book_button.setFont(font)
        self.borrow_book_button.setStyleSheet("QPushButton{\n"
"     border-radius:30px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 63 15pt \"Segoe UI Semibold\";\n"
"    background: rgb(105, 157, 238);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover:!pressed\n"
"{\n"
"background: rgb(105, 157, 238);\n"
"border : 2px solid black;\n"
"}")
        self.borrow_book_button.setObjectName("borrow_book_button")
        self.book_stats_button = QtWidgets.QPushButton(self.frame)
        self.book_stats_button.setGeometry(QtCore.QRect(970, 160, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.book_stats_button.setFont(font)
        self.book_stats_button.setStyleSheet("QPushButton{\n"
"     border-radius:30px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 63 15pt \"Segoe UI Semibold\";\n"
"    background: rgb(105, 157, 238);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover:!pressed\n"
"{\n"
"background: rgb(105, 157, 238);\n"
"border : 2px solid black;\n"
"}")
        self.book_stats_button.setObjectName("book_stats_button")
        self.give_book_button = QtWidgets.QPushButton(self.frame)
        self.give_book_button.setGeometry(QtCore.QRect(670, 160, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.give_book_button.setFont(font)
        self.give_book_button.setStyleSheet("QPushButton{\n"
"     border-radius:30px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 63 15pt \"Segoe UI Semibold\";\n"
"    background: rgb(105, 157, 238);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover:!pressed\n"
"{\n"
"background: rgb(105, 157, 238);\n"
"border : 2px solid black;\n"
"}")
        self.give_book_button.setObjectName("give_book_button")
        self.user_stats_button = QtWidgets.QPushButton(self.frame)
        self.user_stats_button.setGeometry(QtCore.QRect(1270, 160, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.user_stats_button.setFont(font)
        self.user_stats_button.setStyleSheet("QPushButton{\n"
"     border-radius:30px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 63 15pt \"Segoe UI Semibold\";\n"
"    background: rgb(105, 157, 238);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover:!pressed\n"
"{\n"
"background: rgb(105, 157, 238);\n"
"border : 2px solid black;\n"
"}")
        self.user_stats_button.setObjectName("user_stats_button")
        Home.setCentralWidget(self.centralwidget)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        self.welcome_label.setText(_translate("Home", "WELCOME"))
        self.borrow_book_button.setText(_translate("Home", "BORROW BOOK"))
        self.book_stats_button.setText(_translate("Home", "BOOK STATS"))
        self.give_book_button.setText(_translate("Home", "GIVE BOOK"))
        self.user_stats_button.setText(_translate("Home", "USER STATS"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())
