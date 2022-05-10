import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and sqlite3.cursor

class SQLite3:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def create_table(self, table_name, column_name, column_type):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS %s(%s %s)" % (table_name, column_name, column_type))

    def insert(self, table_name, column_name, value):
        self.cursor.execute("INSERT INTO %s(%s) VALUES(?)" % (table_name, column_name), (value,))
        self.conn.commit()

    def select(self, table_name, column_name):
        self.cursor.execute("SELECT %s FROM %s" % (column_name,
