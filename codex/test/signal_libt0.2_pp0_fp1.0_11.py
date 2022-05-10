import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import cv2
import os
import sys
import time
import glob

from PIL import Image

import tensorflow as tf
from tensorflow.keras.models import load_model

from utils import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

   
