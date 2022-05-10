import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from PyQt4 import QtGui
from PyQt4 import QtCore

import mainwindow
import about
import aboutqt
import status
import frame

__version__ = "0.0.0"

def get_version():
    return __version__


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.statusbar = status.StatusBar(self)
        self.setStatusBar(self.statusbar)

        self.statusbar.message("Ready")

        self.about = about.About(self)
        self.aboutqt = aboutqt.AboutQt(self)

        self.frame = frame.Frame(self)
        self.setCentralWidget(self.frame)

