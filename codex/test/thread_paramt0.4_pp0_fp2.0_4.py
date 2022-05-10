import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

from pyqtgraph.ptime import time
from pyqtgraph.dockarea import *

from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType
from pyqtgraph.parametertree import types as pTypes

from pyqtgraph.metaarray import MetaArray
from pyqtgraph import PlotWidget
from pyqtgraph.graphicsItems.LegendItem import LegendItem

from pyqtgraph.widgets.MatplotlibWidget import MatplotlibWidget

from pyqtgraph.graphicsItems.PlotItem.PlotItem import PlotItem
from pyqtgraph.graphicsItems.PlotItem import PlotDataItem
from pyqtgraph.graphicsItems.LegendItem import LegendItem

