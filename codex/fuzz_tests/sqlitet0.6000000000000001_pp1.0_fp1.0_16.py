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

if __name__ == '__main__':
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    my_cb_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    lib.sqlite3_enable_shared_cache(1)
    lib.sqlite3_config(ctypes.c_int(4), my_cb_ptr, ctypes.c_void_p())
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("create table test (id integer primary key autoincrement, foo text);")

    for i in xrange(100):
        conn.execute("insert into test (foo) values (?)", ("foo",))

    conn.commit()

    def do_work():
        conn = sqlite3.connect(DB_URI, uri=True)
        conn.row_factory = sqlite3.Row
        res = conn.execute("select test(foo, ?) as foo
