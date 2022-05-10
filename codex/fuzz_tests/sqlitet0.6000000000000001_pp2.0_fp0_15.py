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

sqlite3.enable_shared_cache(True)

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_shared_cache(1)

sqlite3.sqlite_version_info

try:
    sqlite3.sqlite_version_info
except AttributeError:
    pass
else:
    print("sqlite_version_info was not removed")

sqlite3.sqlite_version

try:
    sqlite3.sqlite_version
except AttributeError:
    pass
else:
    print("sqlite_version was not removed")

sqlite3.complete_statement

try:
    sqlite3.complete_statement
except AttributeError:
    pass
else:
    print("complete_statement was not removed")

sqlite3.complete

try:
    sqlite3.complete
except AttributeError:
    pass
else:
    print("complete was not removed")

sqlite3.threadsafety

try:
   
