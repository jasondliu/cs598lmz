import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Test for Qt bindings
try:
    from PyQt4 import QtGui
    from PyQt4 import QtCore
    from PyQt4.QtCore import pyqtSignal
except ImportError:
    raise ImportError("Cannot import PyQt4, please install it")

# Test for NumPy
try:
    import numpy
except ImportError:
    raise ImportError("Cannot import numpy, please install it")

# Test for OpenCV
try:
    import cv2
except ImportError:
    raise ImportError("Cannot import OpenCV, please install it")

# Test for PySerial
try:
    import serial
except ImportError:
    raise ImportError("Cannot import PySerial, please install it")

# Test for PyGame
try:
    import pygame
except ImportError:
    raise ImportError("Cannot import PyGame, please install it")

