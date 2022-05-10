import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread, pyqtSignal
import time
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

from threading import Thread
from queue import Queue

from scipy.interpolate import interp1d

from scipy.interpolate import interp1d

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg

import serial
import serial.tools.list_ports

class Window(QtGui.QMainWindow):

    def __init__(self):
