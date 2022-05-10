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

class TestExtension(unittest.TestCase):
    def test_load_delete(self):
        """
        Install and remove a tinyDB inside an in-memory db
        """
        self.assertEqual(ctypes.util.find_library('db'), None)
        lib = ctypes.CDLL('./test.so')
        lib.test_load_delete()
        del lib

class TestConnection(unittest.TestCase):
    def test_close(self):
        """
        Check that connections are closed after use
        """
        c = sqlite3.connect(DB_URI, uri=True)
        del c

        self.assertEqual(ctypes.util.find_library('db'), None)

    def test_del(self):
        """
        Check that connections are closed when deleted
        """
        c = sqlite3.connect(DB_URI, uri=True)
        del c

        self.assertEqual(ctypes.util.find_library('db'), None)

class TestBinding(unittest
