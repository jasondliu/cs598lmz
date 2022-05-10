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

sqlite3.sqlite3_thread_cleanup()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
sqlite3.sqlite3_initialize()

libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
libc.pthread_create.restype = ctypes.c_int

thread_id = ctypes.c_ulong()

libc.pthread_create(
    ctypes.byref(thread_id),
    None,
    sqlite3.sqlite3_thread_cleanup,
    None
)

libc.pthread_join(thread_id, None)

sqlite3.sqlite3_shutdown()
