import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# from PyQt4.QtGui import *
# from PyQt4.QtCore import *

from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import QTimer

import time
import datetime

import numpy as np
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random
import sys

import matplotlib.animation as animation


class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")


