import ctypes
import ctypes.util
import threading
import sqlite3
import time

libm = ctypes.CDLL(ctypes.util.find_library('m'), use_errno=True)

class timer:
    def __init__(self):
        self.thread = threading.Timer(2, self.run)
        self.thread.start()
        self.db = sqlite3.connect(':memory:')

    def run(self):
    
        start = time.time()
        self.db.execute('PRAGMA synchronous = OFF;')
        self.db.execute('PRAGMA journal_mode = MEMORY;')
        cur = self.db.cursor()
        cur.execute("create table test (a TEXT);")
        cur.execute("insert into test values ('abc');")
        cur.execute("select * from test")
        res = cur.fetchone()[0]
        cur.execute("delete from test")
        self.db.commit()
        end = time.time()
        print("sqlite insert/select/delete: " + str(end - start))

        mem = ctypes
