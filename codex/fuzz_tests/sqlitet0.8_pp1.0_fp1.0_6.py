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

class MyThread(threading.Thread):
    def run(self, *args, **kwargs):
        r = sqlite3.sqlite3_enable_shared_cache(True)
        assert r == 0

        my_cb_address = ctypes.cast(my_cb, ctypes.c_void_p).value

        r = sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SINGLETHREAD)
        assert r == 0

        r = sqlite3.sqlite3_shutdown()
        assert r == 0

        r = sqlite3.sqlite3_initialize()
        assert r == None

        r = sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
        assert r == 0

        r = sqlite3.sqlite3_wal_hook(ctypes.cast(my_cb_address, ctypes.c_void_p).value)
        assert r == None

        try:
            r = sqlite3.sqlite3_wal_checkpoint
