import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QDialog
from PyQt5.QtGui import QIcon

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_Dialog

from netifaces import interfaces, ifaddresses, AF_INET

import os
import sys
import time
import threading
import json
import socket
import subprocess

from . import utils

class About(QDialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self, parent
