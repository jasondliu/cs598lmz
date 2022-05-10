import ctypes
import ctypes.util
import threading
import sqlite3

import numpy as np

from PyQt4 import QtCore, QtGui

import pyqtgraph as pg

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType



class ParameterTreeWithButtons(ParameterTree):
    def __init__(self, parent=None):
        super(ParameterTreeWithButtons, self).__init__(parent)
        self.setHeaderLabels(['Parameter', 'Value'])
        self.setIndentation(0)
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 200)
        self.setColumnWidth(2, 80)
        self.setColumnWidth(3, 80)
        self.setColumnWidth(4, 80)


class ParameterTreeWithButtonsItem(ParameterItem):
    def __init__(self, param, depth):
        super(ParameterTreeWithButtonsItem, self).__init__(param, depth)
