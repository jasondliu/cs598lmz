import ctypes
import ctypes.util
import threading
import sqlite3
import re
from my_debugger_defines import *
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from Helpers.debugger_signal_constants import DebuggerSignals


class Debugger(QObject):

    report_exception = pyqtSignal(object, dict)
    report_output = pyqtSignal(object, str)
    report_status = pyqtSignal(object, str)

    def __init__(self, parent=None):
        super(Debugger, self).__init__(parent)
        self.h_process = None
        self.pid = None
        self.debugger_active = False
        self.debugger_thread = None
        self.first_breakpoint = None

    @pyqtSlot()
    def load(self, executable):
        # dwCreation flag determines how to create the process
        # set creation_flags = CREATE_NEW_CONSOLE if you want
        # to see the calculator GUI
        creation_flags = DEBUG_PROCESS

        # instantiate
