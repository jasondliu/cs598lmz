import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QListWidget, QListWidgetItem, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

import sys
import os
import re
import subprocess
import time
import threading

from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Docker GUI')
        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))

        self.mainWidget = MainWidget(self)
        self.setCentralWidget(self.mainWidget)


