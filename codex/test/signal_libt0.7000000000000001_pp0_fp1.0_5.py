import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import sys

from pyqtgraph.Qt import QtGui, QtCore

from pyqtgraph.console import ConsoleWidget

from PyQt5.QtCore import QThread, pyqtSignal

import pyqtgraph as pg
# pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

import numpy as np
import cv2

import matplotlib
# matplotlib.use('Qt5Agg')
# import matplotlib.pyplot as plt
# plt.ion()

import sys
import time
import os
import glob

import subprocess as sp

import skimage

