import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time

from PyQt5.QtCore import Qt, QSize, QPoint, QEvent, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QToolTip, QMessageBox, QSystemTrayIcon, QMenu, QAction, QLabel

from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QCheckBox, QSpinBox, QLabel, QFrame, QSizePolicy, QScrollArea, QFileDialog

import numpy as np

import ctypes as ct
import cv2

from skimage.measure import compare_ssim as ssim

class App(QMainWindow):
    def __init__(self):
        super
