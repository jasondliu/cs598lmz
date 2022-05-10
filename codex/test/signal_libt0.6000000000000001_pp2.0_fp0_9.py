import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QAction, QFileDialog, QToolButton, QStyle
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D
import random
import numpy as np
import time
from datetime import datetime
from threading import Thread
import os
import csv
import sys
import serial

class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.left = 10
