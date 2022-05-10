import threading
threading.stack_size(2**27)

import sys
sys.setrecursionlimit(10**7)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

import os
import time
import datetime
import random
import csv

import seaborn as sn
