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

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
lib.sqlite3_shutdown()
lib.sqlite3_config(ctypes.c_int(1), ctypes.c_int(1))
lib.sqlite3_initialize()
lib.sqlite3_open_v2(":memory:", ctypes.byref(my_threading_local.db), ctypes.c_int(1), None)

lib.sqlite3_update_hook(my_threading_local.db, ctypes.c_void_p(my_cb), None)

my_threading_local.db.contents.interrupt()
</code>
The above code works fine on macOS. However, when I run it on Ubuntu 18.04, it crashes with the following error:
<code>python3 test.py
Segmentation fault (core dumped)
</code>
What is the problem?

