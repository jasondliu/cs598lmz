import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class Thread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        self.conn.execute("select * from t")

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_threadsafe.restype = ctypes.c_int
lib.sqlite3_threadsafe()

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table t(x)")
cur.execute("insert into t(x) values (1)")
cur.execute("insert into t(x) values (2)")

t1 = Thread(cur)
t2 = Thread(cur)
t1.start()
t2.start()
t1.join()
t2.join()

con.close()
