import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')
from _sqlite3 import Connection as _Connection

class Connection(sqlite3.Connection):
    """
    A class derived from sqlite3.Connection.  Overrides
    Connection.create_function to provide a lock around
    connection objects.  This allows results of C extension
    functions to be shared.

    """
    def __init__(self, *args):
        self._lock = threading.Lock()
        super(Connection, self).__init__(*args)

    def create_function(self, name, f, argc, deterministic):
        with(self._lock):
            super(Connection, self).create_function(name, argc, f, deterministic)

if __name__ == "__main__":
    lib = ctypes.util.find_library('c')
    if lib is None:
        print("Can't find C library")
        sys.exit(1)

    libc = ctypes.cdll.LoadLibrary(lib)
    libc.getpid.restype = ctypes.c_
