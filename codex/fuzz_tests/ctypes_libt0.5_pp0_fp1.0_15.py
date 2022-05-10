import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import argparse
import traceback
import numpy as np

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSlider, QLineEdit, QFileDialog, QMessageBox

from PyQt5.QtGui import QIcon, QPixmap, QImage, QCursor, QPalette, QBrush

from PIL import ImageGrab
from PIL import Image
from PIL import ImageDraw
from PIL import ImageQt

import cv2
import mss
import pyautogui
import math
import pytesseract
import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
from pytesseract import Output

import pyautogui
import pyscreenshot as ImageGrab
from PIL import Image
import pytesser
