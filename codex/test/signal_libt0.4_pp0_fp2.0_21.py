import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import sys
import os
import random
import time
import numpy as np

from serial import Serial
from serial.tools import list_ports

from scipy.interpolate import interp1d

from datetime import datetime

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class App(QMainWindow):

    def __init__(self):
        super().__init__()
