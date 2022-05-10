import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()


class SQLite3Test(unittest.TestCase):
    def setUp(self):
        self.libsqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

        self.saved_funcs = []
        for name in ('sqlite3_open', 'sqlite3_close', 'sqlite3_exec'):
            self.saved_funcs.append(getattr(self.libsqlite3, name))

    def tearDown(self):
        for name, func in zip(('sqlite3_open', 'sqlite3_close', 'sqlite3_exec'), self.saved_funcs):
            setattr(self.libsqlite3, name, func)

    def test_connect(self):
        self.libsqlite3.sqlite3_open.restype = ctypes.c_void_p
        self.libsqlite3.sqlite3_open.argtypes = [ctypes.c_char_p]

