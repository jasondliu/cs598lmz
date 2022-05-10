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

sqlite3.sqlite3_randomness_hook.restype = ctypes.c_int
sqlite3.sqlite3_randomness_hook.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

sqlite3.sqlite3_randomness(9, None)
sqlite3.sqlite3_randomness_hook(9, my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.cursor().execute("select test(9, 8)")
a.cursor().execute("select test(9, 8)")

t = threading.Thread(target=lambda: getattr(my_threading_local, "a", 1))
t.start()
t.join()

del a
print("del a")

t = threading.Thread(target=lambda: getattr(my_threading_local, "a", 1))
t.start()
