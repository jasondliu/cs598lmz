import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PySide import QtGui
from PySide import QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
from random import randint
import serial
import time
import datetime
import os
from threading import Thread

class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # a figure instance to plot on
        self.figure = pg.PlotWidget(name='Plot1')
        self.figure.setYRange(-1.5,1.5)
        self.figure.setXRange(0,2000)
        self.figure.showGrid(x=True, y=True)

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = self.figure

        # this is the Navigation widget
