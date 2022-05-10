import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class TestSqlite3:

    def setup_class(self):
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'))
        self.libc.sqlite3_threadsafe()

        if self.libc.sqlite3_threadsafe() == 0:
            pytest.skip("sqlite3 not thread safe")

    def test_memory_database(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE foo (bar STRING)")
        conn.execute("INSERT INTO foo (bar) VALUES ('baz')")
        assert conn.execute("SELECT bar FROM foo").fetchone()[0] == 'baz'

    def test_multi_thread(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE foo (bar STRING)")
        conn.execute("INSERT INTO foo (bar) VALUES ('baz')")

