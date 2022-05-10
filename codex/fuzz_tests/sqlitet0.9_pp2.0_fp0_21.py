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

class SQLiteTest(unittest.TestCase):
    def setUp(self):
        global sqlite3
        if sqlite3 is None:
            import sqlite3

    def tearDown(self):
        if hasattr(my_threading_local, 'a'):
            del my_threading_local.a

    def do(self, fn, sql, *rargs):
        if hasattr(my_threading_local, 'a'):
            a = my_threading_local.a
        else:
            a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
            my_threading_local.a = a

        if hasattr(onnx_proto, 'onnx_verify_version'):
            verify_version = onnx_proto.onnx_verify_version
        else:
            verify_version = None
        if verify_version is not None:
            # ensure this test is run with the same protobuf
            # major version in case the on
