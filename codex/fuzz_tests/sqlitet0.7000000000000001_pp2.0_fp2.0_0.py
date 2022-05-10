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

    def test_func(self):
        if sys.platform == "win32":
            return
        db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        db.set_authorizer(my_cb)
        db.execute("select test(1, 2)")
        self.assertEqual(self.get_refcounts_and_free_tids(), [1,1])
        del db
        self.assertEqual(self.get_refcounts_and_free_tids(), [1,1])
        del my_threading_local.a
        self.assertEqual(self.get_refcounts_and_free_tids(), [1,0],
                "the connection should be freed")

    def get_refcounts_and_free_tids(self):
        """
        Returns a list of refcounts and the number of freeable tids.
        """

        cnt = sqlite3.threading.Threading().thread
