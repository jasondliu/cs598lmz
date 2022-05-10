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

ctypes.pythonapi.PyGILState_Ensure.restype = ctypes.c_long
ctypes.pythonapi.PyGILState_Ensure.argtypes = []

ctypes.pythonapi.PyGILState_Release.restype = None
ctypes.pythonapi.PyGILState_Release.argtypes = [ctypes.c_long]

ctypes.pythonapi.PyEval_GetBuiltins.restype = ctypes.c_void_p
ctypes.pythonapi.PyEval_GetBuiltins.argtypes = []

ctypes.pythonapi.PyDict_Check.restype = ctypes.c_int
ctypes.pythonapi.PyDict_Check.argtypes = [ctypes.c_void_p]

ctypes.pythonapi.PyDict_Clear.restype = ctypes.c_int
ctypes.pythonapi.PyDict_Clear.argtypes = [ctypes.c_void_p]

#Used only to import sqlite3.
ctypes.pythonapi.PyRun_String.
