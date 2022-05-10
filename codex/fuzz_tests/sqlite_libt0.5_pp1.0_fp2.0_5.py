import ctypes
import ctypes.util
import threading
import sqlite3
import json

class Db:
    def __init__(self):
        self.db = sqlite3.connect(':memory:', check_same_thread=False)
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS data (name TEXT, value TEXT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS data_meta (name TEXT, value TEXT)')
        self.lock = threading.Lock()

    def set(self, name, value):
        self.lock.acquire()
        self.cursor.execute('DELETE FROM data WHERE name=?', (name, ))
        self.cursor.execute('INSERT INTO data VALUES (?, ?)', (name, value))
        self.db.commit()
        self.lock.release()

    def get(self, name):
        self.lock.acquire()
        self.cursor.execute('SELECT value FROM data WHERE name=?', (name, ))
        row = self.cursor.fetchone
