import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QSize, Qt, QPoint

from tkinter import *
from PIL import Image, ImageTk
from threading import Thread
import time
import sys

from mss import mss
from PIL import Image
from threading import Thread

import socket

# https://stackoverflow.com/questions/40334147/python-3-pyqt-5-qthread-not-working-with-pyqt-signal
class Worker(QtCore.QThread):
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self
