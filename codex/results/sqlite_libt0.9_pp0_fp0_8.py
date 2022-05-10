import ctypes
import ctypes.util
import threading
import sqlite3

lock = threading.Lock()
    
ffi = ctypes.CDLL(ctypes.util.find_library('c'))

class Test(threading.T
