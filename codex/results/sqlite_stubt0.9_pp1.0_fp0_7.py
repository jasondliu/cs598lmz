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
    b = my_threading_local.a

    if b.execute("select test(1, 1)").fetchone()[0] == 1:
        return 1
    else:
        return 0

class SQLiteFunctionTestCase(unittest.TestCase):
    def setUp(self):
        test_support.load_platform_extension(ctypes.util.find_library("sqlite3"))
        assert test_support.is_loadable_platform_extension()

        with sqlite3.connect(test_support.TESTFN, uri=True) as con:
            cur = con.cursor()
            cur.execute("create table test(t1, t2);")

            for i in range(2):
                for j in range(2):
                    for k in range(4):
                        cur.execute("insert into test values (%s, %s);" % (i, j))

            cur.execute("select * from test;")
            con.row_factory = sqlite3.Row
           
