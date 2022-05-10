import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread
from PyQt4.QtGui import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings
from ui_progress import Ui_Progress
from ui_progress_thread import Ui_ProgressThread

from settings import Settings
from progress import Progress
from progress_thread import ProgressThread
from about import About

from ui_main_thread import Ui_MainThread

from main_thread import MainThread

from qt_utils import *

from utils import *

from gpxpy import gpx

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
