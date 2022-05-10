import ctypes
ctypes.cdll.LoadLibrary('libX11.so')
ctypes.cdll.LoadLibrary('libXext.so')


import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as lines
from matplotlib.patches import Ellipse

from Tkinter import *
import Tkinter as tk
import ttk
import tkFileDialog

import serial
import serial.tools.list_ports
import time
import datetime
import threading
import Queue

import numpy as np
import scipy.signal as sp

from scipy.interpolate import UnivariateSpline

from math import pi

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

import pywt

