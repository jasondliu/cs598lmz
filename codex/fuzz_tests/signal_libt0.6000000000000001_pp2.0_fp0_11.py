import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import os.path as path
import re
import math

from PyQt4 import QtGui, QtCore, uic

from numpy import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

from matplotlib.ticker import FormatStrFormatter

from matplotlib.mlab import find

from scipy.interpolate import InterpolatedUnivariateSpline, interp1d

from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

import matplotlib.cm as cm

import pyqtgraph as pg

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree
