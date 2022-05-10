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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(4)

my_cb2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
lib.sqlite3_initialize()
lib.sqlite3_open_v2(b":memory:", ctypes.byref(my_threading_local.db), 0x00000004, None)
lib.sqlite3_create_function_v2(my_threading_local.db, b"my_cb", -1, 0x00000002, my_threading_local.a, my_cb2, None, None, None)
lib.sqlite3_close(my_threading_local.db)
lib.sqlite3_shutdown()
</code>
The code above crashes with the following output:
<code>Exception ignored in: &lt;bound method deleting_conn.__del__ of &lt;__main__.deleting_conn object
