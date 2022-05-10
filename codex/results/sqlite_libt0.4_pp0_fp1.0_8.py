import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import re

from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QIcon, QColor, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QComboBox, QScrollArea, QFrame, QFileDialog, QMessageBox, QProgressBar, QMenuBar, QMenu, QAction, QSizePolicy, QStyle, QStyleFactory, QSystemTrayIcon, QDialog

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.
