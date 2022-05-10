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

libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))
libc.pthread_key_create.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

buf = ctypes.c_void_p(42)
libc.pthread_key_create(ctypes.byref(buf), my_cb)

try:
    libc.pthread_getspecific(buf)
except Exception:
    print("crashed")
</code>
This program should crash, because the reference to <code>a</code> is probably lost after the callback returns. If the destructor of <code>a</code> is called immediately after the callback, it will probably be fine.
However, on Linux, my 18.04 VM crashes, while OSX doesn't. The difference is that OSX uses SQLite 3.15.1, while Linux uses 3.22.0.
The simple change of updating sqlite3 on Linux (by using <code>pip3 install --upgrade</code>) to 3.23.1
