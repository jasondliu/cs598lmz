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


db = sqlite3.connect('test.db')
db.close()

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(ctypes.c_int(3), ctypes.c_int(1))
lib.sqlite3_open("test.db", ctypes.pointer(ctypes.c_void_p()))
lib.sqlite3_open_v2("test.db", ctypes.pointer(ctypes.c_void_p()), ctypes.c_int(0x00000004), ctypes.c_void_p())

threading.Thread(target=my_cb, args=(1,)).start()
lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))

# The following line crashes the process due to a use-after-free.
lib.test_cb(ctypes.c_void_p())
</code>

This is the stacktrace from the failing call in gdb:
<code>Program received
