import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QScrollArea, QCheckBox, QGroupBox, QRadioButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

import numpy as np

import random

import os

from PIL import Image

import cv2

class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'Crop Image'
        self.left = 10
       
