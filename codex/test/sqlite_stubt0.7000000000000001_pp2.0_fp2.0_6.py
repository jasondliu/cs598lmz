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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_vfs_register(sqlite3.sqlite3_vfs_find("unix-none"), 0)
sqlite3.sqlite3_auto_extension(my_cb)

lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
lib.mmap(None, 0x1000, 3, 0x22, -1, 0)
lib.munmap(None, 0x1000)

# This will crash if the above bug is present.
con = sqlite3.connect(DB_URI, uri=True)

cur = con.cursor()
cur.execute("select test(2, 3)")
print(cur.fetchone())
