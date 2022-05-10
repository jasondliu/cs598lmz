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

    return 100


def my_cb2(tup):
    print(tup)
    return 200.

print('Before load')
lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
print('Before init')
lib.sqlite3_initialize()
print('Before thread')
lib.sqlite3_config(lib.SQLITE_CONFIG_MULTITHREAD)
print('Before setting')
lib.sqlite3_progress_handler(9999, my_cb, 0)
print('After setting')

p = lib.sqlite3_malloc(1)

print('Before setting 2')
lib.sqlite3_progress_handler(1006, my_cb2, 0)

print('Before busyloop')
res = lib.sqlite3_busy_handler(p, 123)
print(('res', res, p))
print('End')
