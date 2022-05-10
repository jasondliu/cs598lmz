import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# PyQt imports
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Import the compiled UI module
from ui_mainwindow import Ui_MainWindow

# Import the about dialog
import aboutdlg

# Import the settings dialog
import settingsdlg

# Import the serial port module
import serial

# Import the hexdump module
import hexdump

# Import the version module
import version

# Import the serial port configuration page
import serialportconfig

# Import the QextSerialPort module
import QextSerialPort

# Import the QextSerialEnumerator module
import QextSerialEnumerator

# Import the Qwt module
import Qwt5

# Import the Qwt module
import numpy

# Import the Qwt module
import time

# Import the Qwt module
import math

# Import the Qwt module
import csv

# Import the Qwt module
import os

# Import the Q
