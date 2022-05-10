import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class SQLite3_Connection(object):
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

class SQLite3_Thread(threading.Thread):
    def __init__(self, db_path):
        threading.Thread.__init__(self)
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)
       
