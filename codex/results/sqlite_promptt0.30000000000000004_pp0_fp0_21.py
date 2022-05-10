import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

#import ctypes
#import ctypes.util
#import threading
#import sqlite3
#
#libsqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
#
#class Connection(sqlite3.Connection):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self._lock = threading.Lock()
#        self._lock.acquire()
#        libsqlite.sqlite3_unlock_notify(self._db_handle, self._notify, None)
#        self._lock.release()
#
#    def _notify(self, db, parg):
#        self._lock.acquire()
#        self._lock.release()
#
#    def execute(self, *args, **kwargs):
#        self._lock.acquire()
#        try:
#            return super().execute(*args, **kwargs)
#        finally:
#            self._
