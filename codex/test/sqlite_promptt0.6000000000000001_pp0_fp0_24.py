import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')

# This is the C struct that passes the data to the callback.
class _Data(ctypes.Structure):
    _fields_ = [('id', ctypes.c_int),
                ('rowid', ctypes.c_int64),
                ('value', ctypes.c_double)]

# This is the Python callback that gets called from the C function.
# It simply prints out the data.
def _callback(user_data, data):
    data = ctypes.cast(data, ctypes.POINTER(_Data)).contents
