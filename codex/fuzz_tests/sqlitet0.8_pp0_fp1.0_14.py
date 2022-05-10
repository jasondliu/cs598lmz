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

try:
    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"), ctypes.RTLD_GLOBAL)
    dll.sqlite3_set_authorizer.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    dll.sqlite3_set_authorizer.restype = None

    ctypes.pythonapi.PyThreadState_Get.restype = ctypes.py_object
    ctypes.pythonapi.PyThreadState_Get.argtypes = []

    u = []
    while True:
        x = None
        if hasattr(my_threading_local, "a"):
            x = my_threading_local.a
        print("x:", x)

        y = ctypes.pythonapi.PyThreadState_Get()
        y = ctypes.pythonapi.PyThreadState_Get().c_thread_state.value
        print("y:", y)
        u.append(y)
        if len
