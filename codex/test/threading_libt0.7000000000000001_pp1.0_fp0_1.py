import threading
threading.stack_size(2**27)

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QWidget, QAction, QDialog, QMessageBox, QMainWindow,
                             QApplication, QPushButton, QLineEdit, QLabel,
                             QGridLayout, QVBoxLayout)
from PyQt5.QtGui import QIcon
import sys
import os
import time
import json
import random
import shutil
import sys
import subprocess
import logging

#
#   This is the main window for the app
#   It contains a few buttons and a text window to display the status
#
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Add the menu
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exit
