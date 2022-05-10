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

def my_thread():
    my_threading_local.a.test(2, 3)

libc = ctypes.CDLL(ctypes.util.find_library("c"))

libc.setenv(b"SQLITE_ENABLE_LOAD_EXTENSION", b"1", 1)

sqlite3.sqlite3_extension_init(
    ctypes.c_char_p(b"libsqlitefunctions.so"), None, my_cb)

for x in range(100):
    threading.Thread(target=my_thread, daemon=True).start()
