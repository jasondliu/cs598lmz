import ctypes
import ctypes.util
import threading
import sqlite3

class JsonObj:
    def __init__(self, d):
        self.__dict__ = d

class Sqlite3:
    def __init__(self, filename):
        self.filename = filename
        self.db = sqlite3.connect(filename, check_same_thread=False)
        self.cursor = self.db.cursor()
    def execute(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def close(self):
        self.db.close()

class Base:
    def __init__(self):
        self.conn = sqlite3.connect("data/base.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
