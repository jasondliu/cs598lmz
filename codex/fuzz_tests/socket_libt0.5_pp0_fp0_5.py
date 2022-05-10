import socket
import sys
from threading import Thread
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QTextEdit, QCheckBox, QHBoxLayout, QGroupBox, QRadioButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QSize
#from PyQt5.QtCore import QCoreApplication

# =======================================================================================================================
# =======================================================================================================================

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'GUI'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self
