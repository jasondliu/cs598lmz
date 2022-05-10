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

def main():
    # From sqlite3's docs, this is how to override the default sqlite3_mem_methods
    # https://docs.python.org/3/library/sqlite3.html#custom-memory-management
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MALLOC, ctypes.c_void_p.in_dll(libc, "malloc"))
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MALLOC, ctypes.c_void_p.in_dll(libc, "realloc"))
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MALLOC, ctypes.c_void_p.in_dll(libc, "free"))

    # It seems like the initialization of these functions are thread-specific
    # so we need to initialize it on each thread
    sqlite3.sqlite3_initialize()
