import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import traceback
import threading
import subprocess
import re

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui_mainwindow import Ui_MainWindow

from serial_dialog import SerialDialog
from serial_handler import SerialHandler

from logger import Logger

from user_settings import UserSettings
from settings_dialog import SettingsDialog

from plot import Plot

from data_logger_dialog import DataLoggerDialog

from file_dialog import FileDialog

from data_logger import DataLogger

from about_dialog import AboutDialog

from serial_thread import SerialThread

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.logger = Logger()
        self
