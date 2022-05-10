import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/pi/Desktop/test.db')

class Db(object):
    def __init__(self):
        self.db_name = '/home/pi/Desktop/test.db'
        self.db_table = 'test'
        self.db_column = 'test'
        self.db_value = 'test'
        self.db_conn = sqlite3.connect(self.db_name)
        self.db_cursor = self.db_conn.cursor()
        self.db_cursor.execute('create table if not exists ' + self.db_table + ' (id integer primary key, ' + self.db_column + ' text)')
        self.db_cursor.execute('insert into ' + self.db_table + ' (' + self.db_column + ') values (?)', (self.db_value,))
        self.db_conn.commit()
        self.db_cursor.close()
        self.db_conn.close()

class Gpio(object):
    def __init__(self):
