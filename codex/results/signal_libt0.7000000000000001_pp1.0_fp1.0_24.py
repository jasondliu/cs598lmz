import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import math
import numpy as np
from loader import *

from PyQt5 import QtWidgets, QtGui, QtCore

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

class Viewer(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Iris Viewer")
        self.setWindowIcon(QtGui.QIcon("icon/iris.png"))

    def initUI(self):
        self.main_widget = QtWidgets.QWidget(self)

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.
