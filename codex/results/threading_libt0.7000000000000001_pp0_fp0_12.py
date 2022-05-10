import threading
threading.stack_size(1024*1024)

import multiprocessing
multiprocessing.set_start_method("spawn", True)

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

import sys

from mainwindow import Ui_MainWindow
from utils import *

_translate = QtCore.QCoreApplication.translate

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)

        self.statusBar().showMessage(_translate("MainWindow", "Ready"))

        self.process = QProcess()
        self.process.readyRead.connect(self.readProcess)
        self.process.started.connect(self.started)
        self.
