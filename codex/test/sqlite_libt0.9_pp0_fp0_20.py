import ctypes
import ctypes.util
import threading
import sqlite3
from contextlib import contextmanager
from datetime import datetime

import numpy as np
import scipy.ndimage as ndimage
import scipy.interpolate as interp
import scipy.stats as stats
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg
from PIL import Image

import neodium as neo

neo.configure({
    'nativedebug': True,
    'debug': True,
    'rawdatadir': '/home/adam/.emacs.d/debug',
    'cleanup': True
})

setlocale = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c')).setlocale
setlocale(ctypes.c_int(6), b"en_US")

PKG_NAME = "neoman"

# config options:
