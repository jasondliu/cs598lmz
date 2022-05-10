import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QThread, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QFileDialog, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent, QTextCursor, QStandardItemModel

# Matplotlib
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

# PyAudio
import pyaudio
import wave

# SciPy
import scipy
import scipy.io
import scipy.signal

# Numpy
import numpy as np

# Numexpr
