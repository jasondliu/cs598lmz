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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.create_function.argtypes = [ctypes.c_void_p, ctypes.c_char_p,
                                ctypes.c_int, ctypes.c_void_p]
lib.create_function.restype = ctypes.c_int
addr = lib.create_function(None, b"test", 2, my_cb)
addr = ctypes.c_int.from_address(addr)
print("addr: {}".format(addr))
</code>
Why does this appear to raise a segmentation fault in the <code>sqlite3.connect</code> call?
Update:
Removed the <code>close</code> call entirely, and it still crashes.
<code>import sqlite3

class DeletingConnection(sqlite3.Connection):
    def __del__(self):
        print("JON")

def func(p):
    d = DeletingConnection(DB_URI, uri=True, factory=DeletingConnection)

