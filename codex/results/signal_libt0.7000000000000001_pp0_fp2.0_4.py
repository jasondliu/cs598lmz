import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

###
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
###

from PyQt5.QtWidgets import (QApplication, QWidget,
        QPushButton, QLabel, QTextEdit, QLineEdit, QGridLayout,
        QScrollArea, QFileDialog, QProgressBar, QMessageBox)
        
from PyQt5.QtCore import QThread, pyqtSignal

import subprocess

from reactivity import *

class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1024, 640)
        self.setWindowTitle('reactivity')
        self.setWindowIcon(QIcon('logo.png'))

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        self.label
