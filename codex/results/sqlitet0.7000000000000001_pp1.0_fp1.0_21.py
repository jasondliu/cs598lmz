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

if __name__ == "__main__":
    SQLITE_OPEN_SHAREDCACHE |= 0x00030000
    SQLITE_OPEN_PRIVATECACHE |= 0x00400000
    sqlite3.enable_shared_cache(True)
    c = sqlite3.connect(":memory:")
    c.execute("create table test(a)")
    c.execute("insert into test values (1)")
    c.commit()
    c.close()

    print("shared cache:", ctypes.c_int.in_dll(ctypes.util.find_library("sqlite3"), "sqlite3_open_mode").value & SQLITE_OPEN_SHAREDCACHE)
    print("private cache:", ctypes.c_int.in_dll(ctypes.util.find_library("sqlite3"), "sqlite3_open_mode").value & SQLITE_OPEN_PRIVATECACHE)

    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set
