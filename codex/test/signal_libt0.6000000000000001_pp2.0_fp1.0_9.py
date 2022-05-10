import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QWidget
from PyQt4.QtCore import QTimer

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

from matplotlib import style
import matplotlib.animation as animation
from matplotlib import pyplot as plt

import random
import time

import numpy as np

from scipy.fftpack import fft
from scipy import signal as window

import pyaudio
import struct

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)


