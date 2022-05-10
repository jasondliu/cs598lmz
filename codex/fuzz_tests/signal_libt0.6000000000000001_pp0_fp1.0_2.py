import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QMainWindow, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5 import QtCore
from PyQt5 import QtGui

from PyQt5.QtCore import pyqtSlot

#from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton
#from PyQt5.QtCore import pyqtSlot

import sys
import os
import subprocess
import time
import socket
import threading

import json
import serial
import serial.tools.list_ports
import csv

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib
