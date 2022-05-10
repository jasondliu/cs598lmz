import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_preferences import Ui_Preferences

from utils import *
from settings import *

import os
import sys
import traceback
import json

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(':/icons/icon.png'))
        self.
