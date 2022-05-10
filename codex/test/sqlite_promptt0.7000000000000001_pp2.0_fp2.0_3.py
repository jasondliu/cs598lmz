import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/joshua/Desktop/test.db')
from time import sleep
from collections import deque
import sys
import os
from os.path import join, expanduser

from eoslib import eos_api

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QFrame
from PyQt4.QtGui import QPlainTextEdit, QColor, QPalette, QBrush, QPixmap, QFont, QCursor, QDesktopWidget
from PyQt4.QtCore import QObject, QThread, pyqtSignal, Qt
from PyQt4.QtCore import QSize, QRect, QEvent, pyqtSlot, QPoint

#####################################################################################
#                                Logging class                                      #
#####################################################################################
# class LogThread(QThread):
#     update = pyqtSignal(str)
#     def __init__(self, filename=join(exp
