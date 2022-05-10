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

def my_cb_del(p):
    my_threading_local.a.close()
    del my_threading_local.a
    return 1

def my_cb_del2(p):
    my_threading_local.a.close()
    del my_threading_local.a
    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_set_authorizer(None, my_cb, None)
lib.sqlite3_set_authorizer(None, my_cb_del, None)
lib.sqlite3_set_authorizer(None, my_cb_del2, None)

def main():
    conn = sqlite3.connect(DB_URI, uri=True)
    cursor = conn.cursor()
    cursor.execute("select test(1, 2)")
    cursor.close()
    conn.close()

main()
</code>
The output:
<code>$ python3.3 test.py
Exception ignored in:
