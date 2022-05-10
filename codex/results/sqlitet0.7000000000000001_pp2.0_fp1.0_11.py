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

def test_cb_leak():
    ctypes.pythonapi.PyEval_InitThreads()
    ctypes.pythonapi.PyEval_ReleaseThread(ctypes.pythonapi.PyEval_SaveThread())
    ctypes.pythonapi.PyEval_ReleaseLock()

    ctypes.pythonapi.PyEval_AcquireThread(ctypes.pythonapi.PyEval_SaveThread())

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.create_function("test_cb", 1, my_cb)

    a.execute("SELECT test_cb(1);")

    b = my_threading_local.a

    assert a != b

    a.execute("SELECT test(1, 2);")
    b.execute("SELECT test(1, 2);")

    a.close()
    b.close()

    py_thread_state = ctypes.c_void_p.in_dll(ctypes.pythonapi, "_PyThreadState_Current")
    assert py_
