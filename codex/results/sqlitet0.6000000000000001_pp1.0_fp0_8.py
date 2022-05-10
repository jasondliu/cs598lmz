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

def main():
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))
    lib.sqlite3_initialize()

    callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    lib.sqlite3_open_v2(DB_URI.encode('utf-8'), ctypes.byref(my_threading_local.a), ctypes.c_int(2), ctypes.c_char_p(0), callback)

    my_threading_local.a.execute("SELECT test(1, 2)")

main()
</code>
The problem is that the <code>sqlite3.Connection</code> instance is not being closed after the thread finishes. What am I missing?


A:

<code>sqlite3.Connection</code> is a subclass of <code>sqlite3.C
