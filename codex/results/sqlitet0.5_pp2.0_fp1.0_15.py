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

my_cb_p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

dll_path = ctypes.util.find_library("sqlite3")
dll = ctypes.CDLL(dll_path)

dll.sqlite3_config(ctypes.c_int(1), ctypes.c_void_p(my_cb_p))

conn = sqlite3.connect(DB_URI, uri=True)
conn.execute("select test(1, 2)")
</code>
The issue is that when I run this code, I get this error:
<code>sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 1231453936 and this is thread id 1231453936
</code>
I'm not sure how to fix this, I've tried calling <code>sqlite3_open_v2</code> with <code>SQLITE_OPEN_URI</code> and <code>SQLITE
