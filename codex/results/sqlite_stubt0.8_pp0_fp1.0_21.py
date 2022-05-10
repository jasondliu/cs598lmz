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

lib = ctypes.util.find_library("sqlite3")
if not lib:
    raise Exception("sqlite3 not found")

p = ctypes.CDLL(lib)
p.sqlite3_step.restype = ctypes.c_int
p.sqlite3_step.argtypes = [ctypes.c_void_p]

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

try:
    conn.create_function("test", 2, test_fn)
except:
    pass

curs = conn.cursor()
curs.execute("create table stuff (f1 integer)")
curs.execute("insert into stuff values (?)", (23,))
curs.execute("select test(f1, f1) from stuff")

curs.fetchone()

curs.execute("create temp table temp (f1 integer
