import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from PIL import Image

import os
import sys
import time
import json
import requests
import threading
import subprocess

from utils import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('登录')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(300, 200)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.central_widget = QWidget()
