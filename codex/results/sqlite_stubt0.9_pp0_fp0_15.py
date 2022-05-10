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

def my_cb_final(p):
    my_threading_local.a.close()


class SQLite3Test(unittest.TestCase):
    def test_register(self):
        open = sqlite3.register_adapter(type(open), lambda o: o.name)
        self.assertEqual(open(__file__).read(), __file__)

        f = sqlite3.connect(":memory:")
        f.execute("select ?", (open,))
        result = f.fetchone()
        f.close()
        self.assertEqual(result[0], sqlite3.sqlite_version)

    def test_register_converter(self):
        convert_buffer = sqlite3.register_converter("buffer", buffer)
        self.assertIs(convert_buffer(memoryview("test")), buffer("test"))

        f = sqlite3.connect(":memory:")
        f.row_factory = sqlite3.Row
        f.execute("select ? as text", (memoryview("test
