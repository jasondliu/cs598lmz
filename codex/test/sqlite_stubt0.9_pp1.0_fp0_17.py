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

def my_ui_cb(err, msg):
    print("my_ui_cb: %s; err=%s" % (msg, err))

if hasattr(ctypes, "CDLL"):
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.config(uri=True)
    sqlite3._set_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

    if sqlite3.sqlite_version_number >= 3006023:
        print("Starting work...")
        print("SQLite version: %s" % sqlite3.sqlite_version)
        print("DB_URI: %s" % DB_URI)

        cloud_init = ctypes.CDLL(ctypes.util.find_library("cloud-init"))
