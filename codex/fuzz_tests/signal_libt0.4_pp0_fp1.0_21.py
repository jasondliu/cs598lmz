import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QDesktopWidget, QFileDialog, QTextEdit, QProgressBar
from PyQt5.QtGui import QIcon, QPixmap
import sys
import numpy as np
import os
import cv2
import time
import subprocess
import json
import threading
import queue
import copy
import traceback
import math
import pydicom
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplot
