import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

#import time

class TestSharedCache(unittest.TestCase):

    def setUp(self):
        self.lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
        self.lib.sqlite3_enable_shared_cache(1)
        self.lib.sqlite3_initialize()

    def tearDown(self):
        self.lib.sqlite3_shutdown()

    def test_shared_cache_thread(self):
        db = sqlite3.connect(':memory:', uri=True)
        cursor = db.cursor()
        cursor.execute('CREATE TABLE t (c)')
        cursor.execute('INSERT INTO t VALUES (1)')
        db.commit()
        cursor.execute('SELECT count(*) FROM t')
        self.assertEqual(cursor.fetchone()[0], 1)

        def writer():
            db2 = sqlite3.connect(':memory:', ur
