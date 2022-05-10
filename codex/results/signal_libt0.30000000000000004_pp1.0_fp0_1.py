import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QMessageBox, QTextEdit, QFileDialog
from PyQt5.QtCore import QSize, QThread, pyqtSignal, QObject
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal

import os
import sys

from subprocess import Popen, PIPE

class MyThread(QThread):
    mysignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        while True:
            self.mysignal.emit("test")
            self.
