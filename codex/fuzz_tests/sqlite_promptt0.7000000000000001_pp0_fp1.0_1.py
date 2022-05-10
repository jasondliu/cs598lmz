import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
from collections import namedtuple


# Restart-safe logging
def _log(level, *args):
    global log_level
    if log_level >= level:
        print(*args)
_log_debug = lambda *args: _log(1, 'DEBUG:', *args)
_log_info = lambda *args: _log(2, 'INFO:', *args)
_log_warning = lambda *args: _log(3, 'WARNING:', *args)
_log_error = lambda *args: _log(4, 'ERROR:', *args)


class _Hubs(object):
    def __init__(self):
        self._hubs = []
        self._rlock = threading.RLock()
    def __iter__(self):
        with self._rlock:
            return iter(self._hubs)
    def __contains__(self, hub):
        with self._rlock:
            return hub in self._hubs
    def remove(self, hub):
       
