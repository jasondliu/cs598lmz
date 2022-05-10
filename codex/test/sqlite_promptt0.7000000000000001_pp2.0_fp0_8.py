import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")
# Test sqlite3.connect("/root/test.db")
# Test sqlite3.connect("/root/test.db", uri=True)
# Test sqlite3.connect("file:/root/test.db", uri=True)

# Test sqlite3.connect("/root/test.db", uri=True, check_same_thread=False)

class TestURI(unittest.TestCase):
    def setUp(self):
        self.filename = testlib.uniq_file()
        self.uri = self.filename.replace("\\", "/")

    def test_uri(self):
        self.assertTrue(sqlite3.connect(self.uri, uri=True))

    def test_uri_file(self):
        self.assertTrue(sqlite3.connect("file:" + self.uri, uri=True))

    def tearDown(self):
        testlib.unlink(self.filename)

