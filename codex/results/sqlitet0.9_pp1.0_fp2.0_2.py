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

ctypes.pythonapi.PyEval_SaveThread.argtypes = []
ctypes.pythonapi.PyEval_SaveThread.restype = ctypes.py_object

ctypes.pythonapi.PyEval_AcquireThread.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyEval_AcquireThread.restype = None

p = ctypes.util.find_library("my_lib")
my_lib = ctypes.CDLL(p)

my_lib.my_cb.argtypes = [ctypes.py_object]
my_lib.my_cb.restype = ctypes.c_int

if __name__ == "__main__":
    my_lib.my_cb(my_cb)
</code>
The problem is that in the example above I end up with <code>"sqlite3.Connection object at 0x7f16f99bd880"</code>, which after the connection to <code>a</code> is closed is cleared, instead of <code>"sqlite3.Connection object at 0x7
