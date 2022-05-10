import ctypes
import ctypes.util
import threading
import sqlite3
from enum import Enum
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from rass_interface import *
from speechRecord import *
from speechDetect import *
from musicPlayer import *
from webkit import webkit
try:
    from PyQt5.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = type("")

class MyWindowClass(QtWidgets.QMainWindow, Ui_newMainWindow):
    def __init__(self, parent=None):
        self.setupUi(self)
        #self.songText.setText(self.get_text())
#        self.__current
