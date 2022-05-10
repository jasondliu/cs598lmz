import ctypes
import ctypes.util
import threading
import sqlite3
import os
import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.QtPrintSupport import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Puffin")
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")
        self.setFixedSize(800, 450)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
