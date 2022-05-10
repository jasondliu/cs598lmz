import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import platform
import signal
import subprocess
import json

# The following import is used for the logging module
import logging

# The following import is used for the configparser module
import configparser

# The following import is used for the libusb module
import usb.core
import usb.util

# The following import is used for the PyQt5 module
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# The following import is used for the PyAudio module
import pyaudio

# The following import is used for the matplotlib module
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

# The following import is used for the serial module
import serial

# The following import is used for the pyserial module

