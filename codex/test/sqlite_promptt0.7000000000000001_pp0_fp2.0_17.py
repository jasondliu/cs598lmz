import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("")


class TestSqlite3(unittest.TestCase):
    def SetUp(self):
        # Test sqlite3.connect("", check_same_thread=False)
        self.connection = sqlite3.connect("", check_same_thread=False)

    def TestThreadConnection(self):
        self.connection.execute("CREATE TABLE Test(Id INTEGER PRIMARY KEY, Name TEXT)")
        self.connection.execute("INSERT INTO Test(Name) VALUES (?)", ("Thread",))

        try:
            thread = threading.Thread(target=self.DoThread)
            thread.start()
            thread.join()
        finally:
            self.connection.close()

    def DoThread(self):
        # Test sqlite3.connect("", check_same_thread=False)
        connection = sqlite3.connect("", check_same_thread=False)

