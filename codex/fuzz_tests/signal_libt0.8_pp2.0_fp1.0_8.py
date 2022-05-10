import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pickle
import os,sys
import pylab
from PyQt4.QtCore import QObject, pyqtSlot
from functools import partial
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.widgets import Slider
import numpy as np
from pylab import *


# app=QApplication(sys.argv)
# widget=QMainWindow()
# widget.show()
# sys.exit(app.exec_())


class Window(QtGui.QMainWindow):
    def __init__(self, parent= None):
        QtGui.QMain
