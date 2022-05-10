import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import traceback
import sys
import datetime

from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUi
import ui_main

import config.config
import qt_utils

import numpy as np

import doa.doa

import subprocess

class MainWindow(QtGui.QMainWindow,ui_main.Ui_MainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)

        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.doa_setting)
        self.connect(self.pushButton_3,QtCore.SIGNAL("clicked()"),self.doa_auto)
        self.connect(self.pushButton_4,QtCore.SIGNAL("clicked()"),self.doa_close
