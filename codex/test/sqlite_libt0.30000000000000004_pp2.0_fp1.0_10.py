import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, QTimer
from PyQt5.QtWidgets import QApplication

from . import config
from . import util
from . import log
from . import db
from . import net
from . import ui

class Main(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.app = QApplication(sys.argv)
        self.config = config.Config()
        self.log = log.Log(self)
        self.db = db.DB(self)
        self.net = net.Net(self)
        self.ui = ui.UI(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        self.tick()

    def tick(self):
        self.db.tick()
