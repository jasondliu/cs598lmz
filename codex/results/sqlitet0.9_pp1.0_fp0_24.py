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

class TestThreaded(unittest.TestCase):
    def test_pysqlite_connect_from_thread(self):
        pysqlite_version_number = sqlite3.sqlite_version_number
        if pysqlite_version_number < 3007008:
            self.fail("This test requires sqlite version >= 3.7.8")

        """
        This test currently fails with a segfault because the same
        SQLite connection isn't used. This can be fixed with
        https://github.com/ghaering/pysqlite/commit/1efe03184a4d4b38b3c4f4a7848adf0c8d8b9e9e
        """
        sqlite_version_number = int(sqlite3.sqlite_version.split(".")[0])
        assertion_message = \
            "This test assumes a bug in sqlite < 3.20.0 is fixed"
        self.assertTrue(sqlite_version_number >= 320, assertion_message)

        a = sqlite3.connect(
