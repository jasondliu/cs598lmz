import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np
import time
import sys
import os

from datetime import datetime

from threading import Thread

import serial

from serial.tools import list_ports

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arduino Serial Plotter")
        self.setGeometry(50, 50, 800, 600)

        self.main_widget = QWidget(self)
        self.set
