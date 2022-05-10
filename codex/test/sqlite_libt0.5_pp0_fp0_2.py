import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

if os.name == 'nt':
    import win32api
    import win32con

from PySide.QtCore import *
from PySide.QtGui import *


class WorkerThread(QThread):

    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)
        self.exiting = False
        self.d = 0
        self.m = 0
        self.y = 0

    def __del__(self):
        self.exiting = True
        self.wait()

    def run(self):
        while not self.exiting:
            self.sleep(1)
            self.emit(SIGNAL("updateTime()"))
            self.sleep(1)
            self.emit(SIGNAL("updateTime()"))
            self.sleep(1)
            self.emit(SIGNAL("updateTime()"))

    def updateDate(self, date):
        self.d = date.day()
        self.m = date.month()
        self
