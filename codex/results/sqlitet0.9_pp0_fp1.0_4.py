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

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

sqlite3.enable_callback_tracebacks(True)
sqlite3.sqlite3_thread_cleanup()
if sqlite3.sqlite3_backup_init(sqlite3.sqlite3_backup_init(
    *sqlite3.sqlite3_open_v2(DB_URI,
                             ctypes.c_int(0x00000002),
                             ctypes.c_void_p(None),
                             0),
    None,
    *sqlite3.sqlite3_open_v2(DB_URI,
                             ctypes.c_int(0x00000002),
                             ctypes.c_void_p(None),
                             0)),
    b"main",
    b"main") != 0:
    raise Exception("sqlite3_backup_init")
if sqlite3.sqlite3_backup_step(sqlite3.sqlite3_back
