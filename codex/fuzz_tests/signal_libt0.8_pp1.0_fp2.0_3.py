import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure
from pyqtgraph.Qt import QtCore, QtGui
#import pyqtgraph as pg

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

class QtMpl(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, update_rate=0.001):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.subplots_adjust(left=0, bottom=0, right=1.0, top=1.0, wspace=0.0, hspace=0.0)

        FigureCanvas.__init__(self
