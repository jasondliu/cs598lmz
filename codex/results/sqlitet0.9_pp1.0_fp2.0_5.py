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

    return 10

sqlite3.sqlite3_create_function(None, "m", 1, sqlite3.SQLITE_UTF8, None,
                                ctypes.pythonapi.PyLong_FromLong, None, None,
                                ctypes.pythonapi.PyLong_FromLong)
sqlite3.sqlite3_create_function(None, "tcb", 1, sqlite3.SQLITE_UTF8, None,
                                my_cb, None, None, ctypes.pythonapi.PyLong_FromLong)

class MyTest(unittest.TestCase):

    def setUp(self):
        sqlite3.complete_statement("DROP TABLE IF EXISTS test;")
        con = sqlite3.connect(DB_URI, uri=True)
        cur = con.cursor()
        cur.execute("CREATE TABLE test(t TEXT)")
        cur.execute("INSERT INTO test(t) VALUES ('a')")
        con.commit()
        # Make sure the connection is closed
        con.close()

    def check_completion(
