import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import sys
import os
import numpy as np
import time

from scipy.interpolate import interp1d

from matplotlib.figure import Figure

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from matplotlib.widgets import Slider, Button, RadioButtons

from matplotlib.patches import Rectangle

from matplotlib.lines import Line2D

from matplotlib.colors import LinearSegmentedColormap

from matplotlib.collections import PatchCollection

from matplotlib.patches import Polygon

from matplotlib.colors import Normalize

from matplot
