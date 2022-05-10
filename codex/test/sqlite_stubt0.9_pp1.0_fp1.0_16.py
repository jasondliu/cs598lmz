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
    return 1

pythonapi = ctypes.pythonapi
pythonapi.PyThreadState_SetAsyncExc.argtypes = [
        ctypes.c_long, ctypes.py_object
]
pythonapi.PyThreadState_SetAsyncExc.restype = ctypes.c_int

def kill_thread(tid, excobj):
    tmp = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            tid, ctypes.py_object(excobj)
    )
    if tmp == 0:
        raise ValueError("nonexistent thread id")
    elif tmp > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def main():
    ctypes.CDLL(ctypes.util.find_library("sqlite3"), ctypes.RTLD_GLOBAL)
    d = sqlite3.enable_callback_tracebacks(True)
