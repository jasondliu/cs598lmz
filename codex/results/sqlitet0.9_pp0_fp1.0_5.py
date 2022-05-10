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

class BugTest(unittest.TestCase):

    def test_fixture(self):

        global my_threading_local

        conn = sqlite3.connect(DB_URI, uri=True)

        conn.execute("CREATE TABLE abc(a, b);")

        conn.close()

        self.assertTrue(conn.closed)
        self.assertTrue(my_threading_local.a.closed)

        conn = sqlite3.connect(DB_URI, uri=True)

        conn.execute("INSERT INTO abc VALUES(?, ?);", (1, 2))

        conn.close()

        dlopen = ctypes.cdll.LoadLibrary(ctypes.util.find_library('dl'))

        self.assertTrue(dlopen)

        self.assertEqual(dlopen._testfunc_test_fixture_730922_() , 1)

    def test_fixture_non_shared(self):

        global my_threading_local

        conn = sqlite3.connect(DB_URI, uri=
