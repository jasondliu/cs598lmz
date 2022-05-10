import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# import sqlite3
# db = sqlite3.connect('test.db')
# cursor = db.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, str TEXT, num INTEGER)''')
# cursor.execute('''INSERT INTO test(str, num) VALUES(?, ?)''', ('one', 1))
# cursor.execute('''INSERT INTO test(str, num) VALUES(?, ?)''', ('two', 2))
# cursor.execute('''INSERT INTO test(str, num) VALUES(?, ?)''', ('three', 3))
# db.commit()
# cursor.execute('''SELECT * FROM test''')
# values = cursor.fetchall()
# print(values)
# db.close()

class Sqlite3DB:
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name
        self.db = None
        self.cursor = None
        self.lock
