import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

from PyQt5.QtCore import QThread, pyqtSignal

from . import constants as c
from . import utils


class Executor(QThread):
    """
    Executor class for the executable file.
    """
    data_received = pyqtSignal(str)

    def __init__(self, parent=None):
        """
        Constructor of the Executor class.
        :param parent: parent widget.
        """
        super().__init__(parent)
        self._parent = parent
        self._process = None
        self._std_out = None
        self._std_err = None
        self._return_code = None
        self._lock = threading.Lock()
        self._stop = False
        self._data = ''
        self._data_list = []
        self._data_list_lock = threading.Lock()

    def run(self):
        """
        Override the run method of QThread class.
        """
        self._process = QProcess()
        self._process.
