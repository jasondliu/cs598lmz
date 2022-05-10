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

def my_cb2(p):
    my_threading_local.a.close()
    del my_threading_local.a
    return 1

# Windows:
sqlite3.sqlite3_open(":memory:", ppdb)
# Non-Windows:
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open(":memory:", ppdb)

print sqlite3.sqlite3_create_function(pdb, "testx", 0, 0, None, None, None, None)
print sqlite3.sqlite3_set_authorizer(pdb, my_cb, None)
print sqlite3.sqlite3_exec(pdb, "SELECT test()", None, None, None)
print sqlite3.sqlite3_exec(pdb, "SELECT IFNULL(my_threading_local.a,'missing')", None, None, None)
sqlite3.sqlite3_unlock_notify(pdb, None, None)
print sqlite3.
