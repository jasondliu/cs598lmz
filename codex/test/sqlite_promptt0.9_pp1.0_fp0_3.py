import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb?mode=memory&cache=shared')

libm = ctypes.cdll.LoadLibrary(ctypes.util.find_library('m'))
libpthread = ctypes.cdll.LoadLibrary(ctypes.util.find_library('pthread'))
libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

def atomic_xchange_64(address, new_value):
    old_value = ctypes.c_int64()
    ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(threading.get_ident()), ctypes.py_object(SystemExit))
    libsqlite3.sqlite3_threadsafe()
