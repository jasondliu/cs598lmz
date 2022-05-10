import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import ctypes
import re
import subprocess
import time
import math
import win32gui
import win32api
import win32con
import win32com.client
import win32process
import psutil
import shutil
import cv2
import numpy as np

from PIL import ImageGrab, Image

from win32com.client import GetObject

from PIL import ImageGrab

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QHBoxLayout, QVBoxLayout, QCheckBox, QRadioButton, QGroupBox, QGridLayout, QListWidget, QListWidgetItem, QMessageBox, QSizePolicy, QScrollArea, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap, QImage, QColor, QPainter, QFont
from PyQt5.QtCore import Qt, QObject, pyqtSignal

from threading import
