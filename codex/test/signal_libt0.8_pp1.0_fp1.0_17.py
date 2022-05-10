import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal, QThread, Qt, QCoreApplication
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from multiprocessing import Process, Pipe
from qtpy import QtWidgets, QtCore
from collections import defaultdict
from importlib import import_module
from pkgutil import iter_modules
from pyqtgraph.parametertree import ParameterTree
from pyqtgraph.parametertree import ParameterItem, Parameter
import pyqtgraph
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
import numpy as np
