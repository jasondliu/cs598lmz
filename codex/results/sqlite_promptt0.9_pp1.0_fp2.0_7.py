import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(db_name).cursor().execute('select * from station')
db_name = '/tmp/station.db'
test_sql = 'select * from station'

sqlite3.connect(db_name).cursor().execute(test_sql)

libc = ctypes.CDLL(ctypes.util.find_library('c'))

class ScopedLock(object):
    def __init__(self, lock, name):
        self._lock = lock
        self._name = name

    def __enter__(self):
        print "Entering lock %s" % self._name
        libc.fdatasync(1)
        self._lock.acquire()

    def __exit__(self, *args):
        self._lock.release()
        print "Exiting lock %s" % self._name
        libc.fdatasync(1)

def worker(sql, lock):
    conn = sqlite3.connect(db_name).cursor()
    with ScopedLock(lock, 'shared'):
        print conn.execute(sql
