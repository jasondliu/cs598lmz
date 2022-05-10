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

if __name__ == "__main__":
    sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(ctypes.pointer(my_threading_local.p)), sqlite3.SQLITE_OPEN_URI | sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE, None)

    for i in range(100):
        my_threading_local.a = None
        t = threading.Thread(target=my_cb, args=(my_threading_local.p,))
        t.start()
        t.join()
        my_threading_local.a.execute("select test(1, 2)")
        my_threading_local.a.close()
