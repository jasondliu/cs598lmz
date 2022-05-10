import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph.opengl as gl
import pyqtgraph.exporters
import pyqtgraph.console

from pyqtgraph.ptime import time
from pyqtgraph.dockarea import *
from pyqtgraph.widgets.RawImageWidget import RawImageWidget
from pyqtgraph.widgets.MatplotlibWidget import MatplotlibWidget
from pyqtgraph.widgets.SpinBox import SpinBox
from pyqtgraph.widgets.ValueSpinBox import ValueSpinBox
from pyqtgraph.widgets.ColorButton import ColorButton
from pyqtgraph.widgets.Slider import Slider
from pyqtgraph.widgets.Button import Button
from pyqtgraph.widgets.RadioButton import RadioButton
from pyqtgraph.widgets.CheckBox import CheckBox
from pyqtg
