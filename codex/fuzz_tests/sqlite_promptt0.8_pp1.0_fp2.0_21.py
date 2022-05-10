import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/dev/shm/img.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)


class devShm:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        self.conn.execute('CREATE TABLE IF NOT EXISTS img(name, image, date)')
        try:
            self.len = self.conn.execute('SELECT length(image) FROM img').fetchone()[0]
        except:
            self.len = 100

    def modify(self, name, image, date):
        dpf = self.conn.execute('SELECT date FROM img WHERE name=?', [name]).fetchall()
        if len(dpf) == 0:
            self.conn.execute('INSERT INTO img(name, image, date) VALUES (?,?,?)', [name, image,
