import ctypes
import ctypes.util
import threading
import sqlite3

import numpy as np
import scipy.stats
import scipy.signal
import scipy.fftpack

import matplotlib.pyplot as plt

import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui

from collections import deque

import time

# import the shared library
lib = ctypes.CDLL(ctypes.util.find_library('libread_sensor'))

# define the return type
lib.read_sensor.restype = ctypes.c_float

# define the argument type
lib.read_sensor.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

# create a lock to make the function thread safe
lock = threading.Lock()

# initialize the database
conn = sqlite3.connect('sensor.db')

# create the cursor
c = conn.cursor()

# create the table
c.execute('''CREATE TABLE IF
