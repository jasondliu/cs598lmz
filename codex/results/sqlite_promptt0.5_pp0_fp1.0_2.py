import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
# Test sqlite3.connect('file:memory:?cache=private')

class Connection(object):
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'rb')
        self.size = os.fstat(self.file.fileno()).st_size
        self.mm = mmap.mmap(self.file.fileno(), self.size, access=mmap.ACCESS_READ)
        self.mm.close()
        self.lock = threading.Lock()

    def cursor(self):
        return Cursor(self)

    def execute(self, sql, args=None):
        with self.lock:
            self.mm = mmap.mmap(self.file.fileno(), self.size, access=mmap.ACCESS_READ)
            try:
                return Cursor(self).execute(sql, args)
            finally:
                self.mm.close()

    def executemany(self, sql, args):
        with self
