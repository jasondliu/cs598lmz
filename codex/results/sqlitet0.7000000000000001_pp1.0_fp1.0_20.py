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

if __name__ == '__main__':
    p = ctypes.pointer(ctypes.c_void_p())

    sqlite3.sqlite3_open_v2(":memory:", ctypes.byref(p), 0x00000002, None)

    sqlite3.sqlite3_soft_heap_limit(ctypes.c_int(1024*1024))

    sqlite3.sqlite3_create_function(p, "my_cb", 0, 2, None, my_cb, None, None)

    sqlite3.sqlite3_threadsafe()

    sqlite3.sqlite3_enable_shared_cache(1)

    sqlite3.sqlite3_exec(p, "select my_cb();", None, None, None)

    sqlite3.sqlite3_close(p)
</code>
This is the output of the above code:
<code>&gt;&gt;&gt; python.exe swig_test.py
Traceback (most recent call last):
  File "swig_test.py
