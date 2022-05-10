import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import threading
import subprocess

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Qt5-FFmpeg-HWAccel-Example")

        self.pushButton_play.clicked.connect(self.play)
        self.pushButton_stop.clicked.connect(self.stop)
        self.pushButton_pause.clicked.connect(self.pause)
        self.pushButton_resume.clicked.connect(self.resume)

        self.pushButton_play.setEnabled(True)
