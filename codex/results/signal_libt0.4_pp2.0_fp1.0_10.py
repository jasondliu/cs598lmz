import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np
import random
import os
import subprocess
import time

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QMessageBox, QGridLayout, QFileDialog, QAction, qApp, QLabel, QComboBox, QLineEdit, QCheckBox, QInputDialog, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
from scipy import stats
from scipy.stats import norm

from astropy.io
