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

p = ctypes.pythonapi.PyEval_SaveThread
p.argtypes = []
p.restype = ctypes.py_object

p = ctypes.pythonapi.PyEval_RestoreThread
p.argtypes = [ctypes.py_object]
p.restype = None

p = ctypes.pythonapi.PyGILState_Ensure
p.argtypes = []
p.restype = ctypes.c_int

p = ctypes.pythonapi.PyGILState_Release
p.argtypes = [ctypes.c_int]
p.restype = None

p = ctypes.pythonapi.PyThreadState_Swap
p.argtypes = [ctypes.py_object]
p.restype = ctypes.py_object

p = ctypes.pythonapi.PyThreadState_Get
p.argtypes = []
p.restype = ctypes.py_object

p = ctypes.pythonapi.PyThreadState_Delete
p.argtypes = [ctypes.py_object]
p.rest
