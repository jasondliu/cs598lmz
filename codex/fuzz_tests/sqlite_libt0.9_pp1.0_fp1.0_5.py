import ctypes
import ctypes.util
import threading
import sqlite3
import getopt
import os
import sys
import wave
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import scipy
import time
import tempfile
import json
import math

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Wave_Audio_Recorder():
    def __init__(self, filepath, channels=2, samplewidth=2, sample=16000):
        if ctypes.util.find_library("asound") is None:
            print("出现错误: python-alsaaudio库引用出错!")
            exit(-1)

        self.__filepath = filepath
        self.__channels = channels
        self.__samplewidth
