import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import datetime
import json
import os
import os.path
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

from pyqtgraph import PlotWidget
from pyqtgraph.graphicsItems.LegendItem import ItemSample
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.ptime import time
from pyqtgraph.dockarea import *

from socket import *

from datetime import datetime

from matplotlib import dates
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np
# import the PyQt4 modules for all the commands that control the GUI
