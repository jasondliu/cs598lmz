import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon

from ui_mainwindow import Ui_MainWindow

import sys
import os
import json
import subprocess
import re

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings("QtProject", "Qt Creator")

        self.ui.actionOpen.triggered.connect(self.open)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(
