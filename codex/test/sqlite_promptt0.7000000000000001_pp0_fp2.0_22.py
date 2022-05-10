import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.set_isolation_level(sqlite3.ISOLATION_LEVEL_SERIALIZABLE)
# but sqlite3.ISOLATION_LEVEL_SERIALIZABLE is not implemented in Python 2.6

import sys
import time
import random

class TestCases(unittest.TestCase):
    def setUp(self):
        self.dbapi_name = sqlite3
        self.dbapi = sqlite3
        self.db_module_name = 'sqlite3'
        self.db_module = sqlite3
        self.threads = {}
        self.db_name = 'test'
        self.db = sqlite3.connect(self.db_name)

    def tearDown(self):
        self.db.close()
        os.remove(self.db_name)
        for thread in self.threads.keys():
            self.threads[thread].terminate()

    def test_close_cursor(self):
        c = self.db.cursor()
        c.close()
        self.db.commit
