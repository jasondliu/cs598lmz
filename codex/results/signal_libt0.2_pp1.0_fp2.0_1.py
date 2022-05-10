import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.Qt import QTimer

import cv2
import numpy as np
import os
import sys
import time
import threading
import queue

from utils import *
from config import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Face Recognition')
        self.setFixedSize(800, 600)
        self.initUI()
        self.show()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentral
