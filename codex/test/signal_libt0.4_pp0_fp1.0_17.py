import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt

import sys
import os
import numpy as np
import time
import datetime
import subprocess

import pyqtgraph as pg

from matplotlib.figure import Figure

import pyqtgraph.exporters

from pyqtgraph.Qt import QtCore, QtGui

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType

import pyqtgraph.console

import nidaqmx
from nidaqmx.constants import AcquisitionType, TaskMode
