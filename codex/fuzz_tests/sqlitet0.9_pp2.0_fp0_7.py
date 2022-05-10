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


sqlite3.sqlite3_thread_cleanup = sqlite3.sqlite3_thread_cleanup
sqlite3.sqlite3_thread_cleanup()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_GETMALLOC)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MALLOC, ctypes.c_void_p.in_dll(ctypes.util.find_library("c"), "malloc"), ctypes.c_void_p.in_dll(ctypes.util.find_library("c"), "realloc"), ctypes.c_void_p.in_dll(ctypes.util.find_library("c"), "free"), sqlite3._custom_mem_checking)
sqlite3.sqlite3_soft_heap_limit(100000)
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, True)
sqlite3.sqlite3_config(sqlite3
