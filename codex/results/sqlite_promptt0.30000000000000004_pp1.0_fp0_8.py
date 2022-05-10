import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# from https://github.com/python/cpython/blob/3.7/Lib/test/test_sqlite/dbapi.py

class DBAPITest(unittest.TestCase):

    def setUp(self):
        self.threads = []
        self.connections = []

    def tearDown(self):
        for connection in self.connections:
            connection.close()
        for thread in self.threads:
            thread.join()

    def CheckThreading(self):
        # Test that connections can be shared between threads
        def Connect(results, dsn):
            results.append(sqlite3.connect(dsn))
        results = []
        for i in range(2):
            thread = threading.Thread(target=Connect, args=(results, ":memory:"))
            thread.start()
            self.threads.append(thread)
        for thread in self.threads:
            thread.join()
        self.assertEqual(len(results), 2)
        self.connections.ext
