import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() connection
# problem when coverage run --include=./*.py test_sqlite3.py
# FIXME: unknown problem 


class SQLiteTest(unittest.TestCase):
    def setUp(self):
        self.lock = threading.Lock()
        self.t1 = threading.Thread(target=self.__test_setup)
        self.t2 = threading.Thread(target=self.test_open_database)
        self.t1.start()
        self.t2.start()
        #self.__test_setup()
        #self.test_open_database()

    def tearDown(self):
        os.unlink(self.db)

    def __test_setup(self):
        self.db = u"test.db"
        self.lock.acquire()
        self.conn = sqlite3.connect(self.db)
