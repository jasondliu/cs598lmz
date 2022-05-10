import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import subprocess
import re
import time
import traceback
import threading
import json
import datetime
import requests

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_main import Ui_MainWindow
from ui_settings import Ui_SettingsWindow
from ui_about import Ui_AboutWindow
from ui_log import Ui_LogWindow
from ui_progress import Ui_ProgressWindow

from settings import Settings
from log import Log
from progress import Progress
from about import About

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self
