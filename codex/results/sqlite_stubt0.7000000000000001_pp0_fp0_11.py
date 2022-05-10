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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_thread_cleanup()

cb = sqlite3.SQLiteCallbackType(my_cb)
lib.sqlite3_thread_init(cb)

p = lib.sqlite3_threadsafe()
assert p != 0

t = threading.Thread(target=my_cb, args=(p,))
t.start()
t.join()

lib.sqlite3_thread_cleanup()
</code>

