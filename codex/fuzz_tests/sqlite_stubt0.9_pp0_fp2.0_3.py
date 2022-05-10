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

    return 100


ctypes.CDLL(ctypes.util.find_library("sqlite")).sqlite3_create_disposable_module(
                "test", None, "test", None, my_cb
    )

while True:
    threading.Thread(target=lambda p=0: my_threading_local.a.cursor().execute(
                                                                 "SELECT test(3, 4)")
                    ).start()
