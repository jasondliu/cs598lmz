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

def my_cb2(p):
    my_threading_local.a.execute("SELECT test(1, 2)")
    return 1

def b():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.enable_shared_cache(False)
    sqlite3.set_authorizer(my_cb)
    sqlite3.set_authorizer(my_cb2)

def a():
    b()

libc = ctypes.CDLL(ctypes.util.find_library("c"))

def g():
    for i in range(10):
        libc.malloc(1)

def f():
    b()

    t = threading.Thread(target=g)
    t.start()
    t.join()

a()

f()
</code>
If I run this script, I get the following error:
<code>Exception ignored in: &lt;bound method deleting_conn.__del__ of &lt;sqlite3.Connection object at 0x7f73886a35b
