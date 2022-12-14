# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_stats.ui'
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



class Ui_BookStats(object):
    def setupUi(self, BookStats):
        BookStats.setObjectName("BookStats")
        BookStats.resize(1920, 1080)
        BookStats.setMaximumSize(QtCore.QSize(1920, 1080))
        BookStats.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(BookStats)
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
        self.book_stats_label = QtWidgets.QLabel(self.frame)
        self.book_stats_label.setGeometry(QtCore.QRect(560, 10, 741, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.book_stats_label.setFont(font)
        self.book_stats_label.setStyleSheet("QLabel{\n"
"color: rgb(105, 157, 238);\n"
"background: rgba( 4, 7, 15, 0 );\n"
"}\n"
"")
        self.book_stats_label.setAlignment(QtCore.Qt.AlignCenter)
        self.book_stats_label.setWordWrap(True)
        self.book_stats_label.setObjectName("book_stats_label")
        self.go_to_home = QtWidgets.QPushButton(self.frame)
        self.go_to_home.setGeometry(QtCore.QRect(50, 40, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.go_to_home.setFont(font)
        self.go_to_home.setStyleSheet("QPushButton{\n"
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
        self.go_to_home.setObjectName("go_to_home")
        self.confirm_button = QtWidgets.QPushButton(self.frame)
        self.confirm_button.setGeometry(QtCore.QRect(990, 190, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.confirm_button.setFont(font)
        self.confirm_button.setStyleSheet("QPushButton{\n"
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
        self.confirm_button.setObjectName("confirm_button")
        self.no_of_copies_label = QtWidgets.QLabel(self.frame)
        self.no_of_copies_label.setGeometry(QtCore.QRect(40, 800, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.no_of_copies_label.setFont(font)
        self.no_of_copies_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background: rgb(105, 157, 238);\n"
"}")
        self.no_of_copies_label.setAlignment(QtCore.Qt.AlignCenter)
        self.no_of_copies_label.setObjectName("no_of_copies_label")
        self.book_combobox = QtWidgets.QComboBox(self.frame)
        self.book_combobox.setGeometry(QtCore.QRect(420, 190, 501, 61))
        self.book_combobox.setStyleSheet("QComboBox{\n"
"    background: rgb(105, 157, 238);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(105, 157, 238);\n"
"}")
        self.book_combobox.setObjectName("book_combobox")
        self.no_of_copies_box = QtWidgets.QLabel(self.frame)
        self.no_of_copies_box.setGeometry(QtCore.QRect(390, 800, 201, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.no_of_copies_box.setFont(font)
        self.no_of_copies_box.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background: rgb(105, 157, 238);\n"
"}")
        self.no_of_copies_box.setText("")
        self.no_of_copies_box.setAlignment(QtCore.Qt.AlignCenter)
        self.no_of_copies_box.setObjectName("no_of_copies_box")
        self.no_of_availabel_books_label = QtWidgets.QLabel(self.frame)
        self.no_of_availabel_books_label.setGeometry(QtCore.QRect(610, 800, 451, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.no_of_availabel_books_label.setFont(font)
        self.no_of_availabel_books_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background: rgb(105, 157, 238);\n"
"}")
        self.no_of_availabel_books_label.setAlignment(QtCore.Qt.AlignCenter)
        self.no_of_availabel_books_label.setObjectName("no_of_availabel_books_label")
        self.no_of_availabel_books_box = QtWidgets.QLabel(self.frame)
        self.no_of_availabel_books_box.setGeometry(QtCore.QRect(1070, 800, 201, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.no_of_availabel_books_box.setFont(font)
        self.no_of_availabel_books_box.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background: rgb(105, 157, 238);\n"
"}")
        self.no_of_availabel_books_box.setText("")
        self.no_of_availabel_books_box.setAlignment(QtCore.Qt.AlignCenter)
        self.no_of_availabel_books_box.setObjectName("no_of_availabel_books_box")
        self.no_of_books_taken_label = QtWidgets.QLabel(self.frame)
        self.no_of_books_taken_label.setGeometry(QtCore.QRect(1290, 800, 391, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.no_of_books_taken_label.setFont(font)
        self.no_of_books_taken_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background: rgb(105, 157, 238);\n"
"}")
        self.no_of_books_taken_label.setAlignment(QtCore.Qt.AlignCenter)
        self.no_of_books_taken_label.setObjectName("no_of_books_taken_label")
        self.no_of_books_taken_box = QtWidgets.QLabel(self.frame)
        self.no_of_books_taken_box.setGeometry(QtCore.QRect(1690, 800, 201, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.no_of_books_taken_box.setFont(font)
        self.no_of_books_taken_box.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background: rgb(105, 157, 238);\n"
"}")
        self.no_of_books_taken_box.setText("")
        self.no_of_books_taken_box.setAlignment(QtCore.Qt.AlignCenter)
        self.no_of_books_taken_box.setObjectName("no_of_books_taken_box")
        BookStats.setCentralWidget(self.centralwidget)

        self.retranslateUi(BookStats)
        QtCore.QMetaObject.connectSlotsByName(BookStats)

    def retranslateUi(self, BookStats):
        _translate = QtCore.QCoreApplication.translate
        self.book_stats_label.setText(_translate("BookStats", "BOOK STATS"))
        self.go_to_home.setText(_translate("BookStats", "HOME"))
        self.confirm_button.setText(_translate("BookStats", "CONFIRM"))
        self.no_of_copies_label.setText(_translate("BookStats", "NO OF COPIES :"))
        self.no_of_availabel_books_label.setText(_translate("BookStats", "NO OF AVAILABLE BOOKS :"))
        self.no_of_books_taken_label.setText(_translate("BookStats", "NO OF BOOKS TAKEN :"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookStats = QtWidgets.QMainWindow()
    ui = Ui_BookStats()
    ui.setupUi(BookStats)
    BookStats.show()
    sys.exit(app.exec_())
