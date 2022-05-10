import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() (with path)
libsqlite3 = ctypes.util.find_library("sqlite3")
libsqlite3 = ctypes.CDLL(libsqlite3)

ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.get_ident()), ctypes.py_object(SystemExit)) # pylint: disable=no-member

assert not ctypes.pythonapi.PyErr_Occurred() # pylint: disable=no-member

try:
    # This is the most basic use of sqlite3.connect()
    sqlite3.connect("/etc")
except sqlite3.OperationalError:
    pass

assert not ctypes.pythonapi.PyErr_Occurred() # pylint: disable=no-member

try:
    # This is another basic use of sqlite3.connect()
    sqlite3.connect(":memory:")
except sqlite3.OperationalError:
    pass

assert not ctypes.pythonapi.PyErr_Occurred() # pylint
