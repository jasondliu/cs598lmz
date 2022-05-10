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
    sqlite3.sqlite_open('')
except TypeError:
    # Python < 2.6.14, we need to manually register initializer:
    sqlite3.sqlite_open = sqlite3._sqlite.sqlite_open

ctypes.pythonapi.PyThreadState_SetAsyncExc.argtypes = (ctypes.c_long, ctypes.py_object)

def raise_async_in_thread(thread_id, excobj):
    success = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(excobj))
    if success == 0:
        raise ValueError("nonexistent thread id")
    elif success > 1:
        # """if it returns a number greater than one, you're in trouble, 
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")

success = False

