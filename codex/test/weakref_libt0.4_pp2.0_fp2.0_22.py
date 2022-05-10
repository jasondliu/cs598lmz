import weakref
import os
import sys
import time
import traceback

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from . import utils
from . import actions
from . import widgets
from . import resources
from . import settings

class App(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.setApplicationName("Sketch")
        self.setOrganizationName("Sketch")
        self.setOrganizationDomain("sketch.org")
        self.setApplicationVersion("0.1")
        self.settings = settings.Settings()
        self.mainwindow = MainWindow()
        self.mainwindow.show()
        self.lastWindowClosed.connect(self.quit)
        self.aboutToQuit.connect(self.cleanup)
        self.mainwindow.windowTitleChanged.connect(self.updateWindowTitle)
        self.updateWindowTitle()

