import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from PyQt5.QtGui import QIcon

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About

from ui_file_dialog import Ui_FileDialog

import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure

import matplotlib.pyplot as plt

from scipy.stats import norm

from scipy.optimize import curve_fit

from scipy.special import erf

from scipy.integrate import quad


