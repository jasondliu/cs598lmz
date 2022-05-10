import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt

import sys
import os
import numpy as np
import time
import datetime

import pyqtgraph as pg
import pyqtgraph.exporters

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType

from PyQt4.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

from scipy.signal import butter, lfilter, freqz
from scipy import signal
from scipy.
