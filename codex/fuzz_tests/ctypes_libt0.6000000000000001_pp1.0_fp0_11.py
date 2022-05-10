import ctypes
ctypes.windll.user32.SetProcessDPIAware(True)

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.colors as colors
import matplotlib.cm as mplcm
import matplotlib.colorbar as colorbar
from matplotlib.widgets import Slider, Button, RadioButtons, TextBox

from astropy.io import fits
from astropy.table import Table

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.widgets import RectangleSelector

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QAction, QFileDialog, QLabel
from PyQt5.QtGui import QIcon

#import file_io as io
import qt_functions as qt

#import
