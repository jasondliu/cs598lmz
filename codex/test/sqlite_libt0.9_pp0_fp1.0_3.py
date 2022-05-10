import ctypes
import ctypes.util
import threading
import sqlite3
import os
import threading

class HostsDB(object):
    def __init__(self, dbname):
        self.db_name = dbname
        self.now = int(time.time())
        self.connection = sqlite3.connect(dbname, 60, detect_types=sqlite3.PARSE_DECLTYPES)
        self.connection.execute('pragma temp_store=2');
        self.connection.row_factory = sqlite3.Row
        self.connection.text_factory = str
        self.connection.execute('create table if not exists hosts (name text, ip text, timestamp integer)')
        self.connection.execute('create unique index if not exists name_ip on hosts (name, ip, timestamp)')
        self.connection.commit()

    def update(self, name, ip):
        self.connection.execute('insert into hosts (name, ip, timestamp) values (?, ?, ?)', (name, ip, self.now))
        self.connection.commit()

    def expire(self):
        self.connection.execute
