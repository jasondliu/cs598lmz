import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtGui import QPainter, QPixmap, QColor

from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QFileDialog

from PyQt5.QtCore import QThread, pyqtSignal

import sys
import os
import time
import subprocess
import platform
import threading

import json

import numpy as np

import pyqtgraph as pg

from pyqtgraph.Qt import QtCore, QtGui

import cv2

import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Qt5Agg')
