import socket
import base64
import string
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QLabel, QComboBox, QPushButton, QLineEdit, QTextEdit
from PyQt4.QtGui import QMessageBox, QPalette, QPixmap
from PyQt4.QtCore import QObject, SIGNAL
from PyQt4.QtGui import QApplication
from PyQt4 import Qt
import threading
import random
from thread import *
import time

class user:
    socket = None
    id = None
    host = None
    port = None

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.push
