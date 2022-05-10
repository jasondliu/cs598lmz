import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import logging
import argparse
import datetime
import time
from datetime import timedelta
import threading
from operator import itemgetter

from PyQt5.QtCore import pyqtSignal, QThread, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

from anki.storage import Collection
from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo, askUser

from .utils import stripHTML, getDeckName, getUniqueId
from .constants import *
from .deck import Deck

from .mainwindow import Ui_MainWindow
from .config import Config
from .custom_qthread import CustomQThread


class AWindow(QMainWindow):

    def __init__(self):
        super(AWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setWindowFlags(
            self.window
