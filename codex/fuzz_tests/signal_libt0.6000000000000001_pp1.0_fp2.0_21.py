import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np
import time
import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'EEG Reader'
        self.width = 1200
        self.height = 800
       
