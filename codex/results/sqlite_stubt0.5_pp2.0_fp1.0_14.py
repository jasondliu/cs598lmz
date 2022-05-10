import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def main():
    p = ctypes.c_void_p()
    ctypes.pythonapi.PyGILState_Ensure.restype = ctypes.c_int
    ctypes.pythonapi.PyGILState_Ensure.argtypes = []
    ctypes.pythonapi.PyEval_InitThreads.restype = ctypes.c_void_p
    ctypes.pythonapi.PyEval_InitThreads.argtypes = []
    ctypes.pythonapi.PyGILState_Release.restype = None
    ctypes.pythonapi.PyGILState_Release.argtypes = [ctypes.c_int]
    ctypes.pythonapi.PyEval_SaveThread.restype = ctypes.c_void_p
    ctypes.pythonapi.PyEval_SaveThread.argtypes = []
    ctypes.pythonapi.PyEval_RestoreThread.restype = None
    ctypes.pythonapi.PyEval_RestoreThread.argtypes = [ctypes.c_void_p]
    lib = ctypes
