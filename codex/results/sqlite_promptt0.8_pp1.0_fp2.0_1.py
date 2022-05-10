import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

# Get _opaque_pointer
class _opaque_pointer(ctypes.c_void_p):
    _type_ = ctypes.c_void_p

class _sqlite3(ctypes.Structure):
    _fields_ = [
        ('_opaque_struct', _opaque_pointer)
    ]

sqlite3.sqlite3_threadsafe()

# sqlite3.connect
db = sqlite3.connect(':memory:')
db.close()

# sqlite3.connect from ctypes
sqlite3connect = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3')).sqlite3_open
sqlite3connect.restype = ctypes.c_int
sqlite3connect.argtypes = [ctypes.c_char_p, ctypes.POINTER(_sqlite3)]

db2 = _sqlite3()
sqlite3connect(':memory:', ctypes.byref(db2))

ctypes.cdll.LoadLibrary(ctypes.util.find_library
