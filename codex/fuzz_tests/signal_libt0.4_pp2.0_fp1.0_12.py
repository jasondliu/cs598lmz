import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QCheckBox, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

import sys
import os
import subprocess
import json
import re

from . import ui_main_window
from . import ui_about_dialog

from . import config
from . import util

class MainWindow(QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.setWindowTitle(config.APP_NAME)
        self.setWindowIcon(QIcon(config.APP_
