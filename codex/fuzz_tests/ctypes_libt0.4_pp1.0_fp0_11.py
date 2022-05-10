import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2Wx as NavigationToolbar
import wx
import os
import glob
import pandas as pd
import scipy.io as sio
import scipy.signal as signal
import scipy.stats as stats
import scipy.fftpack as fftpack
import scipy.interpolate as interpolate
import math
import pickle
import time
import datetime
import sys
import re
import h5py
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph.console
import pyqtgraph.parametertree.
