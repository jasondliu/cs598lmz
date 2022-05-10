import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() by reading/writing data from a database used by
# another thread. This should not crash the Python interpreter:
# https://bugs.python.org/issue13308
try:
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
except OSError:
    raise unittest.SkipTest("test works only on unix")

try:
    sqlite3.enable_callback_tracebacks(True)
except AttributeError:
    pass

def datahandler(data):
    pass


class TestThread(threading.Thread):
    def __init__(self, database, table):
        self.database = database
        self.table = table
        super(TestThread, self).__init__()

    def run(self):
        db = sqlite3.connect(self.database, timeout=0.1)
        cursor = db.cursor()
        cursor.execute("CREATE TABLE \"%s\" (x)" % self.table)
        db.close()


class TestThread2(threading.Thread):
   
