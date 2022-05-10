import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/jimmy/.cache/gmusicapi/mobileclient/0d0f7cfb8f6d58b6ee1d9b844f8a0a77', isolation_level=None, check_same_thread=False)

class sdb(object):
    def __init__(self, db_path, db_name):
        self.db_path = db_path
        self.db_name = db_name
        self.db_path_name = self.db_path + self.db_name
        self.db = sqlite3.connect(self.db_path_name, isolation_level=None, check_same_thread=False)
        self.mutex = threading.Lock()

    def __del__(self):
        self.db.close()

    def init(self):
        cursor = self.db.cursor()
        cursor.execute('CREATE TABLE sqlite_sequence(name,seq)')
        cursor.execute('CREATE TABLE Album(id TEXT UNIQUE, title TEXT, artist TEXT, year INTEGER,
