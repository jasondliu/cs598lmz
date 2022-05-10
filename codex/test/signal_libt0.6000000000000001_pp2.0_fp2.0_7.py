import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QSlider, QProgressBar, QLineEdit
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtCore import QTimer
from time import time

import numpy as np
import sys
import os

# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
# from PyQt5.QtCore import QSize
# from PyQt5.QtCore import QTimer
# from PyQt5.QtCore import QRect
# from PyQt5.QtCore import Qt
