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

sqlite3.sqlite3_enable_shared_cache(1)
try:
    sqlite3.sqlite3_global_control(10, 1, my_cb, None)
except ValueError:
    pass

libc = ctypes.CDLL(ctypes.util.find_library("c"))

def my_thread():
    for i in range(2):
        libc.malloc(1024)

        con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        con.execute('select test(1, 2)')

t = threading.Thread(target=my_thread)
t.start()

libc.malloc(1024)

my_threading_local.a.execute('select test(1, 2)')

t.join()
</code>
I have run the test script, and it only fails if I comment out the line <code>sqlite3.sqlite3_global_control(10, 1, my_cb, None)</code>. I have tried this on OS X
