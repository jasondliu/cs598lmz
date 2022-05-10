import ctypes
import ctypes.util
import threading
import sqlite3
import time

from . import util
from . import plugin
from . import cmus

__all__ = ['CmusNotFound', 'CmusNotRunning', 'CmusThread', 'CmusError']

class CmusNotFound(RuntimeError):
    pass

class CmusNotRunning(RuntimeError):
    pass

class CmusError(RuntimeError):
    pass

class CmusThread(threading.Thread):
    def __init__(self, cmuslib):
        threading.Thread.__init__(self)
        self.cmuslib = cmuslib
        self.libcmus = self.cmuslib.libcmus
        self.cmus = self.cmuslib.cmus
        self.running = True
        self.daemon = True
        self._lock = threading.Lock()
        self._ev = threading.Event()
        self._ev.set()
        self.state = cmus.Status()
        self._status = cmus.Status()
        self._changes = set()
        self._handled = set()
       
