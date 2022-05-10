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

# main


sqlite3.enable_load_extension(True)

if ctypes.util.find_library("core"):
    sqlite3.load_extension(os.path.join(os.path.dirname(__file__), "libcore"), ctypes.util.find_library("core"), "core_init")

sqlite3.threadsafety

extdb_handle = sqlite3.extdb()
sqlite3.extdb_open(extdb_handle, b"test", 0)

a = sqlite3.Connection(extdb_handle)

print(a)

