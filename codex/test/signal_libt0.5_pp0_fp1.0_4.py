import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMainWindow, QAction,
                             qApp, QTextEdit, QLineEdit, QGridLayout, QLabel, QFileDialog, QCheckBox, QComboBox, QProgressBar)
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt, QThread, pyqtSignal

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np
import sys
import os
import time
import re
import pandas as pd
import csv
import math

from utils import *
from pca import *
from kmeans import *

