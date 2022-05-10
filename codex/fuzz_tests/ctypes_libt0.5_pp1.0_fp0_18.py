import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

import sys
import os
import random
import time
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from Ui_MainWindow import Ui_MainWindow

import sqlite3

#-----------------------------------------------------

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.init_ui()

        self.init_db()

        self.load_data()

        self.init_signal_slot()

        self.init_timer()

    #-----------------------------------------------------

    def init_ui(self):
        self.setWindowTitle('Программа отсчёта времени
