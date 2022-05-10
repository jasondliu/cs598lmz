import ctypes
import ctypes.util
import threading
import sqlite3
from time import time, sleep
from datetime import datetime
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication, QObject, pyqtSignal

form_class = uic.loadUiType("ui/main_window.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect("db/db.sqlite3")
