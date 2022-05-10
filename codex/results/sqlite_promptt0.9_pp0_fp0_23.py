import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect to see if we are running in a 32-bit or 64-bit Python environment
# If the server is much newer than the client, the test can fail.
conn = sqlite3.connect(':memory:');
try:
    test = ctypes.c_long(1).value
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON')
except sqlite3.ProgrammingError, e:
    if e.args[0].find('DB is not in read/write mode') != -1:
        print 'ERROR: The database is not writable, perhaps it is read only.\nSQLITE3 says:\n', e.args[0]
        sys.exit(-1)
    else:
        raise
if test == 1:
    bt('32')
else:
    bt('64')
if int(bt.btype) == 64 and int(bt.stype) == 32:
    print 'WARNING: Python is a 64-bit build but the SQLite Python library is 32-bit!\n',
    print 'SQLite Python library: ',
