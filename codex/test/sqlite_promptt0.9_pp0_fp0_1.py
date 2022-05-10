import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and sqlite3.Row
sqlite3conn = sqlite3.connect(':memory:')
sqlite3cursor = sqlite3conn.cursor()
sqlite3cursor.execute('CREATE TABLE test (testcol1 TEXT, testcol2 TEXT)')
for k, v in (
    ('foo', 'bar'), ('baz', 'qux'), ('quux', 'quuux'), ('thud', 'grunt'),
):
    sqlite3cursor.execute(
        'INSERT INTO test (testcol1, testcol2) VALUES (?, ?)', (k, v)
    )
sqlite3cursor.execute('SELECT * FROM test')
sqlite3rows12 = list(sqlite3cursor.fetchall())
sqlite3cursor.close()
assert sqlite3.Row == type(sqlite3rows12[0])
def perform_test(conn, cursor):
    if isinstance(conn, sqlite3.Connection):
        assert isinstance(cursor, sqlite3.Cursor)
