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
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn2(a, b):
        return a

    b.create_function("test", 2, test_fn2)

    my_threading_local.b = b

    return 1

threading.Thread(target=my_cb, args=(None,)).start()
threading.Thread(target=my_cb2, args=(None,)).start()

lib = ctypes.PyDLL(ctypes.util.find_library('sqlite3'))

lib.sqlite3_enable_shared_cache(1)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

conn.create_function("test", 2, lambda a, b: a)

print(conn.execute("select test(5, 10)").fetchone()[0])

conn.close()
</code>
The above code prints 5.
But
