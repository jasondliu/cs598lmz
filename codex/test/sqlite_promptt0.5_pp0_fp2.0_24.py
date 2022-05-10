import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def main():
    # Initialize
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.srand(libc.time(0))
    # Test
    test_sqlite3_connect()
    # Finalize
    libc.srand(libc.time(0))

def test_sqlite3_connect():
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE tbl (id INTEGER)')
    db.execute('INSERT INTO tbl VALUES (1)')
    db.execute('INSERT INTO tbl VALUES (2)')
    db.execute('INSERT INTO tbl VALUES (3)')
    db.execute('INSERT INTO tbl VALUES (4)')
    db.execute('INSERT INTO tbl VALUES (5)')
    db.execute('INSERT INTO tbl VALUES (6)')
    db.execute('INSERT INTO tbl VALUES (7)')
