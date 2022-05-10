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

sqlite3.enable_callback_tracebacks(True)

ctypes.pythonapi.PyGILState_Ensure.restype = ctypes.c_long
ctypes.pythonapi.PyGILState_Release.argtypes = (ctypes.c_long,)

def thread_fn(p):
    with p:
        my_threading_local.a = None
        with sqlite3.connect(DB_URI, uri=True) as a:
            my_threading_local.a = a
            a.create_function("test", 2, lambda a, b: a)
            a.execute("select test(1, 2)").fetchone()

t1 = threading.Thread(target=thread_fn, args=(ctypes.pythonapi.PyGILState_Ensure(),))
t1.start()
t1.join()

ctypes.pythonapi.PyGILState_Release(thread_fn.p)
