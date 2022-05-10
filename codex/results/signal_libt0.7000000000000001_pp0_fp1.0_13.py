import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)
import PyQt5
from PyQt5 import QtGui,QtCore,QtWidgets
import sys
import os
import time
import argparse
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import pickle

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QAction,QVBoxLayout,QMessageBox,QSizePolicy,QStatusBar,QToolBar,QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5 import QtWidgets, QtCore

class MyMplCan
