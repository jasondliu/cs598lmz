import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
import numpy as np
import sys
import threading
import time
import os
import serial
import serial.tools.list_ports

from Ui_MainWindow import Ui_MainWindow

class MWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.init_serial()
        self.init_threading()
        self.init_vars()
        self.init_timer()
        self.init_connect()
        self.init_plot()

    def initUI(self):
        self.setWindowTitle('Receiver')
        self.showMaximized()
        self.show()
