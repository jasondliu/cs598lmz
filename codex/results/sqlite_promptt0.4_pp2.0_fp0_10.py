import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)

class Sqlite3Test(unittest.TestCase):
    def setUp(self):
        self.lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
        self.lib.sqlite3_enable_shared_cache(1)
        self.lib.sqlite3_initialize()
        self.db = sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE test(id INTEGER PRIMARY KEY, name TEXT)')
        self.cursor.execute('INSERT INTO test(name) VALUES (?)', ('test',))
        self.cursor.execute('INSERT INTO test(name) VALUES (?)', ('test2',))
        self.db.commit()

    def tearDown(self):
        self.db.close()
        self.
