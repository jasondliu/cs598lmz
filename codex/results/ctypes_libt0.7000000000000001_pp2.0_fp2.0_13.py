import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('myappid')

#import sys
#from os import path

#from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot

import platform
import sys
from os import path
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('myappid')

if platform.system() == "Windows":
    import win32api, win32con

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 statusbar example - pythonspot.com'
        self.left = 10
       
