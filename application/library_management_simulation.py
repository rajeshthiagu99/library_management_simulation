try:
   # pyqt5 packages
   from PyQt5 import QtGui, QtWidgets

   # python packages
   import subprocess
   import sys
   import platform
   import os
   import psutil

   if platform.system() == 'Windows':
      abs_path = (("\\").join((os.getcwd()).split("\\")[:-1])).replace('\\','\\\\')

   if platform.system() == 'Linux':
      abs_path = ("/").join((os.getcwd()).split("/")[:-1])+"/"
   sys.path.insert(0,r'{}'.format(abs_path))

   # import from UI design files.
   from ui_py_files.main_ui import *

   logo_path = os.path.join(abs_path,'qrc_files','logo.ico')
   basedir = os.path.dirname(__file__)
   try:
      from ctypes import windll  # Only exists on Windows.
      myappid = 'mycompany.myproduct.subproduct.version'
      windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
   except:
      pass

   # exit_gracefully function is called when application is about to exit
   def exit_gracefully():
      global home,borrow_book,give_book,book_stats,user_stats

      del home,borrow_book,give_book,book_stats,user_stats
      
      pid = psutil.Process(os.getpid())
      pid.terminate()

   # main application
   if __name__ == "__main__":
      app = QApplication(sys.argv)
      widget = QtWidgets.QStackedWidget()
      app.aboutToQuit.connect(exit_gracefully)

      home = HomeWindow(widget)                               # Home window - 0
      borrow_book = BorrowBookWindow(widget)                  # Borrow Book window - 1
      give_book = GiveBookWindow(widget)                      # Give Book window - 2
      book_stats = BookStatsWindow(widget)                    # Book Stats window - 3
      user_stats = UserStatsWindow(widget)                    # User Stats window - 4

      widget.addWidget(home) 
      widget.addWidget(borrow_book) 
      widget.addWidget(give_book) 
      widget.addWidget(book_stats) 
      widget.addWidget(user_stats) 

      widget.showMaximized()
      widget.setWindowTitle("Library Management System")
      widget.show()

      app.setWindowIcon(QtGui.QIcon(logo_path))
      sys.exit(app.exec_())
except ModuleNotFoundError as moderror:
    module = str(moderror).split("'")[1]

    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',module])
    print('\n',module,' is installed')
    print('--------------------------------------------')
  