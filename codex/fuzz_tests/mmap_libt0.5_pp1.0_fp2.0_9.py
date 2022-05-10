import mmap
import os
import sys
import time

#from numpy import *
#from numpy.linalg import *
#from numpy.random import *
#import numpy as np

from scipy.io import loadmat, savemat
from scipy.signal import lfilter, firwin

from matplotlib import pyplot as plt

import pyqtgraph as pg

from PyQt4 import QtGui, QtCore

from PyQt4.QtCore import QObject, SIGNAL

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

from matplotlib.widgets import Cursor

#from PyQt4.QtCore import *
#from PyQt4.QtGui import *

#from PyQt4.QtCore import pyqtSignal

#from PyQt4.Qt
