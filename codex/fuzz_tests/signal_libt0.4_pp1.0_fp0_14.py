import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import threading
import logging

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox, QFileDialog)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap

from . import lib

class Worker(QThread):
    signal = pyqtSignal(object)

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.signal.emit(self.func(*self.args, **self.kwargs))

class MainWindow(QWidget):
    def __init__(self):
        super().__
