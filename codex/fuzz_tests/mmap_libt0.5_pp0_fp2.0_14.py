import mmap
import os
import sys
import time
import traceback

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.mlab import griddata

# Make sure the pyrogue directory is in the python path
path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, path)

# Make sure the C++ wrapper is compiled
import PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as QtWid

from pyrogue.pydm.data_plugins.image_plugin import ImagePlugin
from pyrogue.pydm.data_plugins.line_plot_plugin import LinePlotPlugin
from pyrogue.pydm.data_plugins.scatter_plot_plugin import ScatterPlotPlugin
from pyrogue.pydm.data_plugins.table_plugin import TablePlugin

from pyrogue.
