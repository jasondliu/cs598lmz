import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import subprocess
import shutil
import re
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_mainwindow import Ui_MainWindow

from config import *
from utils import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("%s %s" % (APP_NAME, APP_VERSION))

        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.init_menu()
        self.init_toolbar()
        self.init_statusbar()

