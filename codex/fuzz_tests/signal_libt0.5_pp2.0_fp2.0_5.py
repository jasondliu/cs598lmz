import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

import sys
import os
import time
import subprocess
import json
import shutil
import re

from ui_mainwindow import Ui_MainWindow

import cv2
import numpy as np

from math import exp

from PyQt5.QtGui import QImage, QPixmap

import serial
import serial.tools.list_ports

import threading

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__
