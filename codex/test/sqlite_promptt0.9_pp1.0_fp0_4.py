import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/tmp/test.db") except DBError
#
# DBError: file is encrypted or is not a database


class DBError(Exception):
    pass
# Main initializer

class DB(sqlite3.Connection):
    def __init__(self, sqlite_file):

        self.lock = Lock(sqlite_file)
        super(DB, self).__init__(sqlite_file)
        self.cursor = self.cursor()
        self.cursor.execute('PRAGMA foreign_keys = ON')
        self.cursor.execute('PRAGMA synchronous = OFF')
        self.write_status = 'off'
        self.state_callback = None
        self.sqlite_file = sqlite_file

    def __del__(self):
        self.close()

    def __clear__(self):
        self.cursor.execute('DROP TABLE IF EXISTS \'mMP3scended\'')
        self.commit()

