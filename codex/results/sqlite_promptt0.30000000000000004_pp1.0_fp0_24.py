import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import time

import numpy as np

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

import matplotlib.pyplot as plt

import matplotlib.dates as mdates

import matplotlib.animation as animation

import matplotlib.patches as patches

from matplotlib.collections import PatchCollection

import matplotlib.patheffects as PathEffects

from matplotlib.widgets import RectangleSelector

import matplotlib.cm as cm

from matplotlib.colors import Normalize

import matplotlib.gridspec as gridspec

from matplotlib.backends.backend_
