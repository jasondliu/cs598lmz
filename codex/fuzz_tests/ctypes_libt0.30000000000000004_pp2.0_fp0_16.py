import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import os
import sys
import time
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QIcon, QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject

from utils import *
from yolo_utils import *
from yolo_model import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initModel()
        self.initData()

    def initUI(self):
        self.setWindowTitle('YOLOv3
