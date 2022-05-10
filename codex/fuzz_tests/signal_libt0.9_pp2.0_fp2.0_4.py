import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtTest import QTest
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSignature

import basic
import flow
import baseparser

import os
import time

class Thread(QtCore.QThread):

    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.exiting = False

    def __del__(self):
        self.exiting = True
        self.wait()

class BasicParserThread(Thread):

    def __init__(self, wnd, flowmgr, baseparser, parent = None):
        Thread.__init__(self, parent)
        self.wnd = wnd
        self.flowmgr = flowmgr
        self.baseparser = baseparser

    def run(self):
        while True:
            baseparser = self.bas
