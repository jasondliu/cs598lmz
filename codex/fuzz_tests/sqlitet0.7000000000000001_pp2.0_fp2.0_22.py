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

def test_callbacks():
    ctypes.pythonapi.PyGILState_Ensure.argtypes = None
    ctypes.pythonapi.PyGILState_Ensure.restype = ctypes.c_long

    ctypes.pythonapi.PyGILState_Release.argtypes = [ctypes.c_long]
    ctypes.pythonapi.PyGILState_Release.restype = None

    sqlite3.sqlite_version_info
    dll = ctypes.util.find_library("sqlite3")
    ctypes.cdll.LoadLibrary(dll)
    sqlite3.sqlite_version_info

    sqlite3.enable_callback_tracebacks(True)
    sqlite3.register_adapter(int, lambda x: float(x))
    sqlite3.register_converter("int", int)
    sqlite3.register_converter("int", int)

    sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    my_cb_p = ctypes
