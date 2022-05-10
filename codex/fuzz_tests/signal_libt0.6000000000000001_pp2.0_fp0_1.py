import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import threading
import Queue

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.Ui_main import Ui_MainWindow
from ui.Ui_settings import Ui_Settings
from ui.Ui_about import Ui_About

import data
import logic

class FileLoader(QThread):

    def __init__(self, parent, filename):
        QThread.__init__(self, parent)
        self.parent = parent
        self.filename = filename

    def run(self):
        self.parent.loadFile(self.filename)
        self.parent.fileLoaded.emit()

class FileSaver(QThread):

    def __init__(self, parent, filename):
        QThread.__init__(self, parent)
        self.parent = parent
        self
