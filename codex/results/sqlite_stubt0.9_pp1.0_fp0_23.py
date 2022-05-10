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

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dll_name = ctypes.util.find_library("SQLite\\Extensions\\SQLite\\Connection")
        self.dll_handle = ctypes.CDLL(self.dll_name)
        self.dll_cb = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
        self.dll_func = self.dll_handle['sqlite3_extension_init']
        self.dll_func.restype = ctypes.c_int
        self.dll_func.argtypes = [self.dll_cb, ctypes.POINTER(ctypes.c_char_p)]
        self.dll_handle['sqlite3_open'].restype = ctypes.c_int
        self.dll_handle['sqlite3_open'].argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))]


