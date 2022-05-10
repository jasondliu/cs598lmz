import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

from gui import Ui_MainWindow

import sys
import os

import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

import time

import serial
import serial.tools.list_ports

import threading

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.thread = threading.Thread(target=self.arduino_serial)
        self.thread.daemon = True
        self.thread.start()

        self.pushButton_2
