import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("C:\\Users\\Admin\\Desktop\\test.db")

class _SQLite3(object):
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def create(self, table, col_name):
        col_name_str = ','.join(col_name)
        sql = "CREATE TABLE IF NOT EXISTS %s(%s)" % (table, col_name_str)
        self.cursor.execute(sql)
        self.conn.commit()

    def insert(self, table, value):
        value_str = ','.join(['?' for i in range(len(value))])
        sql = "INSERT INTO %s VALUES(%s)" % (table, value_str)
        self.cursor.execute(sql, value)
        self.conn.commit()

    def select(self,
