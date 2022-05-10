import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Sqlite3(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.db = sqlite3.connect(db_file)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def executemany(self, sql, values):
        self.cursor.executemany(sql, values)
        self.db.commit()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def query_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def query_one_value(self, sql):
        self.cursor.execute(sql)
