import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')
import qdarkstyle
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QMainWindow)
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
from datetime import datetime
from classes import *
from mainwindow import *
from addnew import *
from changeinfo import *
from menu import *
from addinfo import *
from change_pass import *
from login import *

# Виджет главного окна
class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtWidgets.Q
