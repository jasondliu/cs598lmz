import lzma
lzma.LZMAFile
"""

# -*- coding: latin-1 -*-

import os
import sys
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import cv2
import numpy
import socket
import struct
import copy

# from threading import Thread
# from threading import Lock
import threading
import time
import io
# import picamera

import gc

import random


progname = os.path.basename(sys.argv[0])
progversion = "0.1"

MAX_BASE_KINECT_PORT = 50040
MAX_KINECT_PORT = 50050
MAX_HEIGHT = 480
MAX_WIDTH = 640

APPEND_MODE = "
