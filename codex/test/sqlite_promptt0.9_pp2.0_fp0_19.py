import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections

# An implementation of a Connection in Python
class MyConnection(object):
    def __init__(self, *args, **kwargs):
        self.connection = kwargs.get("connection")

# Using a Global lock for simplicity to serialize connection
# This is not required if the connections have their own lock
# from their respective implementations
connectionLock = threading.Lock()

def _setup_prototypes(lib_name, sqlite_lib):
    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.py_object))
    prototype(("sqlite3_open", sqlite_lib))
