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

def my_cb_3(p):
    for i in range(100):
        my_threading_local.a.execute("SELECT test(?);", (i,)).fetchone()
    return 1

class B(object):
    def __del__(self):
        pass

if __name__ == "__main__":
    sqlite3.enable_callback_tracebacks(True)

    lib = ctypes.CDLL(ctypes.util.find_library("python%d.%d" % sys.version_info[:2]))
    lib.PyEval_GetCurrentThreadId.restype = ctypes.c_int64
    lib.PyEval_SaveThread.restype = ctypes.c_void_p
    lib.PyEval_RestoreThread.argtypes = (ctypes.c_void_p,)

    b = B()
    v = []
    for i in range(1):
        v.append(b)

    tid = lib.PyEval_GetCurrentThreadId()
