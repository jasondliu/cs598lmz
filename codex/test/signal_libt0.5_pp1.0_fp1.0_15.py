import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt4 import QtGui

from gui import Ui_MainWindow
from server import Server
from models import *
from PyQt4.QtCore import *

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.tabWidget.setTabEnabled(3, False)
        self.ui.tabWidget.setTabEnabled(4, False)
        self.ui.tabWidget.setTabEnabled(5, False)
        self.ui.tabWidget.setTabEnabled(6, False)
