import codecs
codecs.register(codecs.lookup('mbcs'))

from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib
from scipy.interpolate import interp1d
from scipy import signal
from scipy.signal import butter, filtfilt
import numpy as np
from pathlib import Path
from pylsl import StreamInlet, resolve_stream
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, \
    QAction, QFileDialog, QMainWindow, QSlider, QSpacerItem, QSizePolicy, QRadioButton

import colorama
from colorama import Fore, Back, Style
colorama.init()

from utils import get_file
