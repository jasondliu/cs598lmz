import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()

class TestConnection(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")

    def tearDown(self):
        self.con.close()

    def CheckPragma(self, con):
        cur = con.cursor()
        cur.execute("pragma table_info('sqlite_master')")
        self.assertEqual(cur.fetchall(), [])
        cur.close()

    def CheckThreads(self, con):
        # Check that the connection can be shared across threads
        def Check():
            self.CheckPragma(con)
        t = threading.Thread(target=Check)
        t.start()
        t.join()

    def CheckNamed(self):
        # Check that the connection can be shared across threads
        con2 = sqlite3.connect(":memory:", check_same_thread=False)
        self.CheckPragma(con2)
        con2.close()

   
