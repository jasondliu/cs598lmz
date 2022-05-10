import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import math
import time
import random

from PyQt4 import QtCore, QtGui
# from PyQt4.QtCore import QThread

from macros import *

from lib.ui_lib import *
from lib.qt_lib import *
from lib.text_lib import *
from lib.audio_lib import *

from UI.qtdesigner.ui_hackingtutor_main_window import Ui_HackingTutor_MainWindow

import lib.btnlib as btnlib
import lib.btnlib_qt as btnlib_qt
import lib.txtlib_qt as txtlib_qt

# Static variables

QT_VERSION_STR = QtCore.QT_VERSION_STR
PYQT_VERSION_STR = QtCore.PYQT_VERSION_STR

# Ui

class HackingTutor_MainWindow(QtGui.QMainWindow):

	def __init__(self):
		super(HackingTutor_MainWindow, self).__init__()


