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

try:
    sqlite3.sqlite3_enable_shared_cache(1)
except AttributeError:
    print("Shared cache disabled")

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)
sqlite3.sqlite3_shutdown()

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_memdebug_backtrace(1)
lib.sqlite3_memdebug_dump("memdbg_dump.txt")

sqlite3.sqlite3_memdebug_fail(-1)

sqlite3.sqlite3_profile(my_cb, 0)

a = sqlite3.connect(DB_URI, uritrue=True, factory=deleting_conn)
a.close()
del a

a = sqlite3.connect(
