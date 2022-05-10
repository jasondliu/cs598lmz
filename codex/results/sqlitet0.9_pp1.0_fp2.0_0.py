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

sqlite_zapi = ctypes.CDLL(ctypes.util.find_library("sqlite"))
sqlite_zapi.sqlite3_shutdown()

sqlite_zapi.sqlite3_initialize()
sqlite_zapi.sqlite3_shutdown()

sqlite3.sqlite_version_info

buf = ctypes.create_string_buffer(1000)
sqlite_zapi.sqlite3_config(2, my_cb, buf)
sqlite_zapi.sqlite3_initialize()
sqlite3.connect(DB_URI)
sqlite3.connect(DB_URI).execute("select test(1, 2)").fetchall()

threading.Thread(target=lambda: sqlite3.connect(DB_URI).execute("select test(1, 2)").fetchall()).start()
threading.Thread(target=lambda: sqlite3.connect(DB_URI).execute("select test(1, 2)").fetchall()).start()
threading.Thread(target=lambda: sqlite3
