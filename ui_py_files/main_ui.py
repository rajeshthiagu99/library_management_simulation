# pyqt5 packages
from PyQt5.QtWidgets import *

# python packages
import platform
import os
import sys
import pandas as pd 
import datetime
import numpy as np

if platform.system() == 'Windows':
   abs_path = (("\\").join((os.getcwd()).split("\\")[:-1])).replace('\\','\\\\')
if platform.system() == 'Linux':
   abs_path = ("/").join((os.getcwd()).split("/")[:-1])+"/"
sys.path.insert(0,r'{}'.format(abs_path))

# ui_python files
from ui_py_files.home import Ui_Home
from ui_py_files.borrow_book import Ui_BorrowBook
from ui_py_files.give_book import Ui_GiveBook
from ui_py_files.book_stats import Ui_BookStats
from ui_py_files.user_stats import Ui_UserStats
from qrc_files import images_rc

# global widget dictionary declaration
widget_dict = {'home':0,'borrow_book':1,'give_book':2,'book_stats':3,'user_stats':4}

user_data_df = pd.read_csv(os.path.join(abs_path,'csv_files','user_data.csv'))
book_data_df = pd.read_csv(os.path.join(abs_path,'csv_files','book_data.csv'))
log_data_df = pd.read_csv(os.path.join(abs_path,'csv_files','log_data.csv'))

def message_box(text):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(text)
    msgBox.setWindowTitle("Information")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec_()



class HomeWindow(QMainWindow):
    def __init__(self,widget):
        QMainWindow.__init__(self)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        QMainWindow.showMaximized(self)
        self.widget=widget

        self.ui.borrow_book_button.clicked.connect(self.openborrowbookwindow)
        self.ui.give_book_button.clicked.connect(self.opengivebookwindow)
        self.ui.book_stats_button.clicked.connect(self.openbookstatswindow)
        self.ui.user_stats_button.clicked.connect(self.openuserstatswindow)
    
    def openborrowbookwindow(self):
        self.widget.setCurrentIndex(widget_dict['borrow_book'])
    
    def opengivebookwindow(self):
        self.widget.setCurrentIndex(widget_dict['give_book'])
    
    def openbookstatswindow(self):
        self.widget.setCurrentIndex(widget_dict['book_stats'])
    
    def openuserstatswindow(self):
        self.widget.setCurrentIndex(widget_dict['user_stats'])

    def __del__(self):
        print()

class BorrowBookWindow(QMainWindow):
    def __init__(self,widget):
        QMainWindow.__init__(self)
        self.ui = Ui_BorrowBook()
        self.ui.setupUi(self)
        QMainWindow.showMaximized(self)
        self.widget=widget

        self.ui.user_id_combobox.addItems(['USER ID'] + [str(user_id) for user_id in user_data_df['user_id'].unique().tolist()])
        self.ui.user_id_combobox.setStyleSheet("background: rgb(105, 157, 238);color: rgb(255, 255, 255);font: 75 12pt 'MS Shell Dlg 2';")
        self.ui.book_combobox.addItems(['BOOKS'] + book_data_df['book_name'].unique().tolist())
        self.ui.book_combobox.setStyleSheet("background: rgb(105, 157, 238);color: rgb(255, 255, 255);font: 75 12pt 'MS Shell Dlg 2';")
        self.ui.confirm_button.clicked.connect(self.confirm)
        self.ui.go_to_home.clicked.connect(self.openhomewindow)
    
    def confirm(self):
        if self.ui.user_id_combobox.currentText() != 'USER ID' and self.ui.book_combobox.currentText() != 'BOOKS':
            user_id = self.ui.user_id_combobox.currentText()
            book_name = self.ui.book_combobox.currentText()
        
            if book_data_df[book_data_df['book_name']==book_name]['in_out'].any():
                book_id = str(book_data_df[(book_data_df['book_name']==book_name)&(book_data_df['in_out']==True)].head(1)['book_id'].values[0])
                shelf_position = str(book_data_df[(book_data_df['book_name']==book_name)&(book_data_df['in_out']==True)].head(1)['shelf_position'].values[0])
                today = (datetime.datetime.strptime(str(datetime.datetime.now().date()), "%Y-%m-%d")).strftime("%d-%m-%Y")

                log_data_df.loc[len(log_data_df)] = [str(len(log_data_df)+1),user_id,book_id,today,np.nan]
                log_data_df.to_csv(os.path.join(abs_path,'csv_files','log_data.csv'),index=False)

                book_data_df.loc[book_data_df['book_id']==int(book_id),'in_out']=False
                book_data_df.to_csv(os.path.join(abs_path,'csv_files','book_data.csv'),index=False)

                self.ui.status_label.setText(f'Thank you please take book from shelf {shelf_position} and goto home')
                self.ui.status_label.setStyleSheet('color: rgb(77, 254, 0);background: rgba( 4, 7, 15, 0 );')
            else:
                self.ui.status_label.setText('Book is not available please choose other book')
                self.ui.status_label.setStyleSheet('color: red;background: rgba( 4, 7, 15, 0 );') 
        elif self.ui.user_id_combobox.currentText() != 'USER ID':
            message_box('Please choose book to borrow book')
        elif self.ui.book_combobox.currentText() != 'BOOKS':
            message_box('Please choose user id to borrow book')
        else:
            message_box('Please choose user id and book to borrow book')

    def openhomewindow(self):
        self.ui.user_id_combobox.clear()
        self.ui.user_id_combobox.addItems(['USER ID'] + [str(user_id) for user_id in user_data_df['user_id'].unique().tolist()])
        self.ui.book_combobox.clear()
        self.ui.book_combobox.addItems(['BOOKS'] + book_data_df['book_name'].unique().tolist())
        self.ui.status_label.setText('')
        self.widget.setCurrentIndex(widget_dict['home'])

    def __del__(self):
        print()

class GiveBookWindow(QMainWindow):
    def __init__(self,widget):
        QMainWindow.__init__(self)
        self.ui = Ui_GiveBook()
        self.ui.setupUi(self)
        QMainWindow.showMaximized(self)
        self.widget=widget

        self.ui.user_id_combobox.addItems(['USER ID'] + [str(user_id) for user_id in user_data_df['user_id'].unique().tolist()])
        self.ui.user_id_combobox.setStyleSheet("background: rgb(105, 157, 238);color: rgb(255, 255, 255);font: 75 12pt 'MS Shell Dlg 2';")
        self.ui.user_id_combobox.activated.connect(self.display_borrowed_books)
        self.ui.book_combobox.addItems(['BOOKS'])
        self.ui.book_combobox.setStyleSheet("background: rgb(105, 157, 238);color: rgb(255, 255, 255);font: 75 12pt 'MS Shell Dlg 2';")
        self.ui.shelf_combobox.addItems(['SHELF POSITION'] + [str(shelf_position) for shelf_position in book_data_df['shelf_position'].unique().tolist()])
        self.ui.shelf_combobox.setStyleSheet("background: rgb(105, 157, 238);color: rgb(255, 255, 255);font: 75 12pt 'MS Shell Dlg 2';")
        self.ui.confirm_button.clicked.connect(self.confirm)
        self.ui.go_to_home.clicked.connect(self.openhomewindow)
    
    def display_borrowed_books(self):
        if self.ui.user_id_combobox.currentText() != 'USER ID':
            self.ui.book_combobox.clear()
            self.ui.book_combobox.addItems(['BOOKS'])
            user_id = self.ui.user_id_combobox.currentText()
            self.ui.book_combobox.addItems([str(book_id) for book_id in log_data_df[(log_data_df['date_in'].isna())&(log_data_df['user_id']==int(user_id))]['book_id'].values.tolist()])
        else:
            self.ui.book_combobox.clear()
            self.ui.book_combobox.addItems(['BOOKS'])

    def confirm(self):
        if self.ui.user_id_combobox.currentText() != 'USER ID' and self.ui.book_combobox.currentText() != 'BOOKS' and self.ui.shelf_combobox.currentText() != 'SHELF POSITION':
            user_id = self.ui.user_id_combobox.currentText()
            book_id = self.ui.book_combobox.currentText()
            user_shelf_position = self.ui.shelf_combobox.currentText()
            shelf_position = str(book_data_df[book_data_df['book_id']==int(book_id)]['shelf_position'].unique().tolist()[0])
            if user_shelf_position == shelf_position:
                today = (datetime.datetime.strptime(str(datetime.datetime.now().date()), "%Y-%m-%d")).strftime("%d-%m-%Y")

                log_data_df.loc[(log_data_df['user_id']==int(user_id))&(log_data_df['book_id']==int(book_id)),'date_in']=today
                log_data_df.to_csv(os.path.join(abs_path,'csv_files','log_data.csv'),index=False)

                book_data_df.loc[book_data_df['book_id']==int(book_id),'in_out']=True
                book_data_df.to_csv(os.path.join(abs_path,'csv_files','book_data.csv'),index=False)

                self.ui.status_label.setText('Thank you please visit again and goto home')
                self.ui.status_label.setStyleSheet('color: rgb(77, 254, 0);background: rgba( 4, 7, 15, 0 );')
                self.display_borrowed_books()
            else:
                self.ui.status_label.setText(f'Please keep the book at shelf {shelf_position}')
                self.ui.status_label.setStyleSheet('color: red;background: rgba( 4, 7, 15, 0 );')
        elif self.ui.user_id_combobox.currentText() == 'USER ID' and self.ui.book_combobox.currentText() != 'BOOKS' and self.ui.shelf_combobox.currentText() != 'SHELF POSITION':
            message_box('Please choose user id to give book')
        elif self.ui.user_id_combobox.currentText() != 'USER ID' and self.ui.book_combobox.currentText() == 'BOOKS' and self.ui.shelf_combobox.currentText() != 'SHELF POSITION':
            message_box('Please choose book to give book')
        elif self.ui.user_id_combobox.currentText() != 'USER ID' and self.ui.book_combobox.currentText() != 'BOOKS' and self.ui.shelf_combobox.currentText() == 'SHELF POSITION':
            message_box('Please choose shelf position to give book')
        elif self.ui.user_id_combobox.currentText() == 'USER ID' and self.ui.book_combobox.currentText() == 'BOOKS' and self.ui.shelf_combobox.currentText() != 'SHELF POSITION':
            message_box('Please choose user id and book to give book')
        elif self.ui.user_id_combobox.currentText() == 'USER ID' and self.ui.book_combobox.currentText() != 'BOOKS' and self.ui.shelf_combobox.currentText() == 'SHELF POSITION':
            message_box('Please choose user id and shelf position to give book')
        elif self.ui.user_id_combobox.currentText() != 'USER ID' and self.ui.book_combobox.currentText() == 'BOOKS' and self.ui.shelf_combobox.currentText() == 'SHELF POSITION':
            message_box('Please choose book and shelf position to give book')
        else:
            message_box('Please choose user id, book and shelf position to give book')

    def openhomewindow(self):
        self.ui.user_id_combobox.clear()
        self.ui.user_id_combobox.addItems(['USER ID'] + [str(user_id) for user_id in user_data_df['user_id'].unique().tolist()])
        self.ui.book_combobox.clear()
        self.ui.book_combobox.addItems(['BOOKS'])
        self.ui.shelf_combobox.clear()
        self.ui.shelf_combobox.addItems(['SHELF POSITION'] + [str(shelf_position) for shelf_position in book_data_df['shelf_position'].unique().tolist()])
        self.ui.status_label.setText('')
        self.widget.setCurrentIndex(widget_dict['home'])

    def __del__(self):
        print()

class BookStatsWindow(QMainWindow):
    def __init__(self,widget):
        QMainWindow.__init__(self)
        self.ui = Ui_BookStats()
        self.ui.setupUi(self)
        QMainWindow.showMaximized(self)
        self.widget=widget

        self.ui.book_combobox.addItems(['BOOKS'] + book_data_df['book_name'].unique().tolist())
        self.ui.book_combobox.setStyleSheet("background: rgb(105, 157, 238);color: rgb(255, 255, 255);font: 75 12pt 'MS Shell Dlg 2';")
        self.ui.confirm_button.clicked.connect(self.confirm)
        self.ui.go_to_home.clicked.connect(self.openhomewindow)
    
    def confirm(self):
        if self.ui.book_combobox.currentText() != 'BOOKS':
            book_name = self.ui.book_combobox.currentText()
            self.ui.no_of_copies_box.setText(str(len(book_data_df[book_data_df['book_name']==book_name])))
            self.ui.no_of_availabel_books_box.setText(str(len(book_data_df[(book_data_df['book_name']==book_name)&(book_data_df['in_out']==True)])))
            self.ui.no_of_books_taken_box.setText(str(len(book_data_df[(book_data_df['book_name']==book_name)&(book_data_df['in_out']==False)])))
        else:
            message_box('Please choose book to see stats')

    def openhomewindow(self):
        self.ui.book_combobox.clear()
        self.ui.book_combobox.addItems(['BOOKS'] + book_data_df['book_name'].unique().tolist())
        self.ui.no_of_copies_box.setText('')
        self.ui.no_of_availabel_books_box.setText('')
        self.ui.no_of_books_taken_box.setText('')
        self.widget.setCurrentIndex(widget_dict['home'])

    def __del__(self):
        print()

class UserStatsWindow(QMainWindow):
    def __init__(self,widget):
        QMainWindow.__init__(self)
        self.ui = Ui_UserStats()
        self.ui.setupUi(self)
        QMainWindow.showMaximized(self)
        self.widget=widget

        self.ui.user_id_combobox.addItems(['USER ID'] + [str(user_id) for user_id in user_data_df['user_id'].unique().tolist()])
        self.ui.user_id_combobox.setStyleSheet("background: rgb(105, 157, 238);color: rgb(255, 255, 255);font: 75 12pt 'MS Shell Dlg 2';")
        self.ui.confirm_button.clicked.connect(self.confirm)
        self.ui.go_to_home.clicked.connect(self.openhomewindow)
    
    def confirm(self):
        if self.ui.user_id_combobox.currentText() != 'USER ID':
            user_id = self.ui.user_id_combobox.currentText()
            self.ui.no_of_books_read_box.setText(str(len(log_data_df[log_data_df['user_id']==int(user_id)])))
            self.ui.no_of_inhand_books_box.setText(str(len(log_data_df[(log_data_df['user_id']==int(user_id))&(log_data_df['date_in'].isna())])))
        else:
            message_box('Please choose user id to see stats')

    def openhomewindow(self):
        self.ui.user_id_combobox.clear()
        self.ui.user_id_combobox.addItems(['USER ID'] + [str(user_id) for user_id in user_data_df['user_id'].unique().tolist()])
        self.ui.no_of_books_read_box.setText('')
        self.ui.no_of_inhand_books_box.setText('')
        self.widget.setCurrentIndex(widget_dict['home'])

    def __del__(self):
        print()
