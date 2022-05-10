import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import logging
logger = logging.getLogger(__name__)


def _load_library():
    lib_path = ctypes.util.find_library('sqlite3')
    if lib_path is None:
        raise OSError("Cannot find libsqlite3")
    return ctypes.CDLL(lib_path)


class _ConnectionSharedState(object):
    def __init__(self, lib):
        self.lib = lib
        self.lock = threading.Lock()
        self.handles = {}

    def get_handle(self, dbapi_connection):
        with self.lock:
            if dbapi_connection in self.handles:
                return self.handles[dbapi_connection]
            else:
                handle = self.lib.sqlite3_open_v2(
                    ':memory:',
                    ctypes.byref(ctypes.c_void_p()),
                    sqlite3.SQLITE_OPEN_READWRITE |
