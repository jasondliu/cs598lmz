import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import pickle
import random
import time
import pyqtgraph as pg
import numpy as np

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.connect(self.ui.actionLoad_Image, QtCore.SIGNAL('triggered()'), self.load_image)
        self.connect(self.ui.actionSave_Data, QtCore.SIGNAL('triggered()'), self.save_data
