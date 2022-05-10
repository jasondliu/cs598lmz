import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
import time

import numpy as np
from numpy import random

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.backend_bases import key_press_handler
from matplotlib.widgets import Slider
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import Cursor
from matplotlib.widgets import TextBox
from matplotlib.widgets import AxesWidget
from matplotlib.widgets import SpanSelector

from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
from scipy.signal import medfilt
from scipy.signal import find_peaks_
