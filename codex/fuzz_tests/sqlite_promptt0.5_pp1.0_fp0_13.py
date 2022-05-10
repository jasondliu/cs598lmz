import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

#import zmq
#import zmq.utils.jsonapi as json

class Db(object):
    def __init__(self, db_file=':memory:'):
        self.db = sqlite3.connect(db_file)
        self.db.text_factory = str
        self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                               devices (id INTEGER PRIMARY KEY,
                                        name TEXT,
                                        type TEXT,
                                        description TEXT,
                                        location TEXT,
                                        status TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                               device_values (id INTEGER PRIMARY KEY,
                                              device_id INTEGER,
                                              name TEXT,
                                              value TEXT,
                                              timestamp TEXT)''')


    def get_devices(self):
        self.cursor.execute('SELECT * FROM devices')
        return self.
