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

clib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
clib.atexit.argtypes = [ctypes.CFUNCTYPE(ctypes.c_int)]
clib.atexit.restype  = ctypes.c_int
clib.atexit(clib.atexit(ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)))
# clib.atexit(clib.atexit(ctypes.CFUNCTYPE(ctypes.c_int)(lambda : None)))

def test_callback_survives(sl):
    sl.execute("select test(1, 2);")
    assert sl.fetchone()[0] == 1
</code>


A:

What you are doing is an abuse of <code>atexit</code> and is not guaranteed to work. For example, according to the documentation, <code>atexit</code> may not be called if the process is killed by a signal. However, this use case will work if the process is killed immediately by a signal
