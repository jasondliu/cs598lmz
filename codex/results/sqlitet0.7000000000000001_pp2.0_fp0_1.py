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

def test_callback():
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open_v2(
        DB_URI,
        ctypes.byref(ctypes.c_void_p()),
        0x00000002 | 0x00000004 | 0x00004000,
        None
    )
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb, allowed=1)
    a = sqlite3.connect(DB_URI, uri=True)
    a.execute("select test(1, 2)")
    del my_threading_local.a
    del a
    # The following code causes a crash:
    # sqlite3.threadsafety = 0

print("This script will crash if the bug is not fixed.")

th = threading.Thread(target=test_callback)
th.start()
th.join()
