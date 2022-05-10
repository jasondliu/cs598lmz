import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QTimer, QThread, SIGNAL
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QDialog, QMessageBox, QInputDialog, QLineEdit, QFileDialog
from PyQt4.uic import loadUiType

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt

import numpy as np
import time
import datetime
import os
import sys
import glob
import csv
import collections
import serial
import serial.tools.list_ports
import threading
import Queue

from matplotlib import rcParams
rcParams['font.size'] = 9

# Ui_MainWindow, QMainWindow = load
