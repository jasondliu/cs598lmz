import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import math
import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QApplication, QMessageBox, QFileDialog)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt

from scipy import signal as sg
from scipy.fftpack import fft
from scipy.signal import butter, lfilter

import pyqtgraph as pg

import serial
import serial.tools.list_ports

import threading

import csv

from datetime import datetime

import warnings
warnings.filterwarnings("ignore")

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

class MainWindow(QWidget):

    def __init
