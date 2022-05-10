import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal

import os
import sys
import time
import subprocess

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings

from settings import Settings
from logger import Logger
from worker import Worker

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = Settings()
        self.logger = Logger()

        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionSettings.trig
