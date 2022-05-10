import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets, QtCore, QtGui

import sys
import os
import json

import h5py
import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap

import pyqtgraph as pg
from pyqtgraph.Point import Point

from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

from pprint import pprint

import struct

import skimage
import skimage.filters
import skimage.morphology
import skimage.segmentation

import time

