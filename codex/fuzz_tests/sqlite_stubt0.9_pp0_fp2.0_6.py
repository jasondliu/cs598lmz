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

dB = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn, check_same_thread=False)

dB.enable_load_extension(True)

dB.execute('select load_extension(?)', (ctypes.util.find_library('sqlitefunctions'),))

dB.create_function("mult", 2, lambda x, y: x * y)
dB.create_function("foo", 5, my_cb)
dB.execut
