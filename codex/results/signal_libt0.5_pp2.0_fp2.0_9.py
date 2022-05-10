import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.animation as animation
from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons


import os
import sys

import pickle

import time
import datetime
import random

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FixedLoc
