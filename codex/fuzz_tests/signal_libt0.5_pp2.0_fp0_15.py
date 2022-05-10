import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QWidget, QPushButton, QComboBox, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QTextEdit, QGroupBox, QCheckBox, QProgressBar, QDialog, QMessageBox
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, QTimer, QSize
from PyQt5.QtGui import QIcon, QPixmap

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import sys
import time
import logging
import os

