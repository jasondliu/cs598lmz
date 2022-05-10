import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt

import sys
import os

import numpy as np
import pandas as pd

import scipy.interpolate as interp
import scipy.integrate as integrate

import time

class AppForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle('Spectral Analysis')
        
        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()
        
