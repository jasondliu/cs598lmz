import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWebEngineWidgets import *

import os, sys
from PIL import Image
from PIL.ImageQt import ImageQt
import cv2
import numpy as np
import matplotlib.pyplot as plt
import qimage2ndarray
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('My App')

        layout = Q
