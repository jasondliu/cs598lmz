import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from time import time
from math import *
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backend_bases import key_press_handler
from matplotlib.widgets import RectangleSelector
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.lines import Line2D
import matplotlib.image as mpimg
from skimage import measure
from scipy import ndimage
from matplotlib import cm
import matplotlib.gr
