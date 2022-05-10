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
    print data

# This is the C function that gets called in a separate thread.
# It executes the specified SQL and then calls the callback.
def _thread_func(db, sql, callback, user_data):
    # Callback is a function pointer, so we need to convert it.
    c_callback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)(callback)

    # This is the C code that executes the specified SQL.
