import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons

from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay

import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import Figure
