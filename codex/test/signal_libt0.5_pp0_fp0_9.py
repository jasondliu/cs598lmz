import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
os.environ['QT_API'] = 'pyside2'

import sys
import time
import numpy as np
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import QObject, Signal, Slot, Property, QThread, QRunnable, QThreadPool, QCoreApplication
from PySide2.QtGui import QPixmap, QImage, QColor, QPainter, QPen, QBrush
from PySide2.QtWidgets import QMainWindow, QWidget, QLabel, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QFileDialog, QGroupBox, QComboBox, QMessageBox
import cv2
import cv2.aruco as aruco

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
