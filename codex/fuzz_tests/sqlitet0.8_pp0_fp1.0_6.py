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

def my_cb2(p):
    a = my_threading_local.a
    if a and not a.closed:
        a.close()

    return 1

class CustomCheckpoint(object):
    def __init__(self):
        self.lib = None
        self.iface_ptr = None
        self.iface = None

    def setup(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library('cpython3.6'))
        self.iface_ptr = self.lib.get_tracing_hook_interface()
        self.iface = ctypes.cast(self.iface_ptr, ctypes.POINTER(ctypes.c_void_p * 9)).contents
        self.iface[5] = ctypes.pythonapi.PyCapsule_New(self, b"test", None)
        self.iface[7] = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_voidp)(my_cb)
        self.iface
