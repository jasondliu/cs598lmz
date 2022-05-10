import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect callable without parameters


class MyConnection(sqlite3.Connection):
    def __init__(self, *args):
        pass


class MyThread2(threading.Thread):
    def run(self):
        self.conn = sqlite3.connect(database="no-such-db", factory=MyConnection)


t2 = MyThread2()
t2.start()
t2.join()
del t2

# Test SQLiteConnection_CreateWithType
if ctypes.util.find_library("sqlite3"):
    cdll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
