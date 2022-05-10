import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('database.db').execute('CREATE TABLE IF NOT EXISTS test (t)').fetchall()
# Test sqlite3.connect('database.db').execute('INSERT INTO test VALUES (?)', [time.time()]).fetchall()

# Dropbox
DB_FILE = 'database.db'

# Pointgray camera
PG_DEVICE_ID = 0
PG_FRAME_WIDTH = 640
PG_FRAME_HEIGHT = 480
PG_FRAME_FORMAT = 'Y8'
PG_FRAME_RATE = 30
PG_AUTO_GAIN = False
PG_GAIN = 0.0
PG_AUTO_SHUTTER = False
PG_SHUTTER = 0.0

FRAME_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

class Frame(object):
    def __init__(self, data, timestamp):
        self.data = data
        self.timestamp = timestamp
        
    def to_string(self):
        return 'Frame(tim
