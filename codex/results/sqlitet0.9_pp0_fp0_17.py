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

class MyTestCase(unittest.TestCase):
    def test_1(self):
        sqlite3.enable_callback_tracebacks(True)

        lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        lib.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), 1)
        lib.sqlite3_initialize()

        conn = sqlite3.connect(DB_URI, uri=True)
        conn.create_collation("test", my_cb)
        conn.execute("create table test(a);")
        conn.execute("insert into test(a) values ('d');")
        junk = conn.execute("select * from test order by a collate test desc;").fetchall()
        del junk
        del conn

        lib.sqlite3_shutdown()
        lib.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_URI), 0)

if __name__ == '__main__':

