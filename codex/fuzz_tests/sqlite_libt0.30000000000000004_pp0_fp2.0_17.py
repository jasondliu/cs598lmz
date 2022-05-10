import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import subprocess
import re

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QThread, SIGNAL

import config
import utils
import ui_main

class MainWindow(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("%s v%s" % (config.APP_NAME, config.APP_VERSION))
        self.setWindowIcon(QtGui.QIcon(config.APP_ICON))

        self.connect(self.actionExit, QtCore.SIGNAL('triggered()'), self.close)
        self.connect(self.actionAbout, QtCore.SIGNAL('triggered()'), self.about)
        self.connect(self.actionAboutQt, QtCore.SIGNAL('triggered()'), self
