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


class Test(unittest.TestCase):
    def test_threaded(self):
        conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        conn.create_function("test", 0, my_cb)

        c = conn.cursor()
        c.execute("select test()")
        c.fetchone()
        conn.commit()
        conn.close()

def test_suite():
    suite = unittest.makeSuite(Test)
    suite.addTest(doctest.DocTestSuite(sqlite3))
    return suite


if __name__ == "__main__":
    #from sqlite3 import dbapi2 as sqlite
    #from pysqlite2 import dbapi2 as sqlite
    import sys

    sqlite_version = "%s.%s.%s" % sqlite3.sqlite_version_info
    print("SQLite version %s" % sqlite_version)
    print("pysqlite %s.%s.%s
