import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QThread, pyqtSignal, QObject
import sys
import os
import json
from PyQt5.QtGui import QFont

import MainWindow

class Main(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.logic = Logic()

        if not os.path.exists("bin"):
            os.mkdir("bin")
        if not os.path.exists("bin/logs"):
            os.mkdir("bin/logs")

        self.updateTimer = QThread()
        self.updateTimerLogic = UpdateTimerLogic(self)
        self.updateTimerLogic.moveToThread(self.updateTimer)
        self.updateTimer.start()

        self
