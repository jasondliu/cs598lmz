import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import subprocess
from datetime import datetime
from time import sleep

class Sqlite3Lock:
    def __init__(self, db, timeout=0):
        self.db = db
        self.timeout = timeout
        self.lock = threading.Lock()
        self.lock_name = 'sqlite3_lock'
        self.lock_id = 0

    def __enter__(self):
        self.lock.acquire()
        self.lock_id = self.db.execute('SELECT random()').fetchone()[0]
        sql = 'INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES (?, ?, ?, ?, ?)'
        self.db.execute(sql, ('table', self.lock_name, self.lock_name, 0, 'CREATE TABLE sqlite_lock (id INTEGER PRIMARY KEY)'))
        self.db.commit()
        while True:
            sql = 'INSERT INTO sqlite_lock (id) VALUES (?)'
