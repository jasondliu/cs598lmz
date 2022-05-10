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

def test_basic():
    # Init sqlite:

    simg = ctypes.CDLL(ctypes.util.find_library('simg'))
    sqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

    simg_config = simg.simg_config
    simg_config.argtypes = [ctypes.c_ulong]
    simg_config.restype = None

    simg_config(1) # SIMG_CONFIG_ENABLE_TRIGGERS

    sqlite3.simg_init()
    sqlite3.sqlite3_create_function_with_trampoline.restype = ctypes.c_int

    # Initialize test function:
    simg_my_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    result = sqlite3.sqlite3_create_function_with_trampoline("simpleconnect", 1, ctypes.addressof(simg_my
