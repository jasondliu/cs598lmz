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

cb_func = sqlite3.SQLITE_STATIC(ctypes.c_int)(my_cb)
cb_func.argtypes = (ctypes.c_void_p,)

try:
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open(":memory:".encode(), ctypes.byref(my_threading_local.database_ref))

    lib.sqlite3_extended_result_codes(my_threading_local.database_ref, 1)

    lib.sqlite3_shutdown()
except AttributeError:
    print(f"{threading.get_ident()} in ctypes error")

try:
    connect = sqlite3.connect(DB_URI, uri=True)
    connect.sqlite_trace(test)

    connect.executescript("create table test (num);")

    cursor = connect.cursor()
    cursor.execute("insert into test values (0);")
    cursor.execute("delete from test
