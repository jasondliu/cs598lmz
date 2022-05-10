import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

import sys
import os

from ui_mainwindow import Ui_MainWindow

import numpy as np

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from matplotlib.figure import Figure

import matplotlib.image as mpimg

import cv2

import time

import threading

import math

import serial

import serial.tools.list_ports

from scipy.interpolate import interp1d

from scipy.optimize import curve_fit

import scipy.ndimage as ndimage

import scipy.ndimage.filters as filters

from scipy import signal

import scipy.stats as stats

import
