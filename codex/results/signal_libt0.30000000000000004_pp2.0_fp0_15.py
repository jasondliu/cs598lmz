import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import os
import subprocess
import time
import threading
import queue
import re

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
        self.q = queue.Queue()
        self.t = threading.Thread(target=self.worker)
        self.t.start()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,
