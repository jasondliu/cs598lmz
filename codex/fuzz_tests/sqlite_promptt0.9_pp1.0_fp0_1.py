import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect if this is python 2.5
try:
    a = sqlite3.connect(":memory:")
    del a
except:
    try:
        lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
    except:
        raise
class Connection(object):
    def __init__(self, path='mdb.sqlite3'):
        self.lock = threading.Lock()
        self.conn = sqlite3.connect(path)
        self.create_database()
        self.tablenames = [x[0] for x in self.conn.execute(
                'select name from sqlite_master where type=\'table\'').fetchall()]

    def _gettype(self, typ):
        return {'str': 'string',
                'int': 'integer',
                'float': 'real',
                }[typ]

    def create_database(self):
        self.conn.execute('CREATE TABLE IF NOT EXISTS groups (geom)\
                           ');
        self.conn
