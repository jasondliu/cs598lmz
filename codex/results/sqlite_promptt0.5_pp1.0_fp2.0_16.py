import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/tmp/test.db')
# Test sqlite3.connect(':memory:')

# Test sqlite3.connect(':memory:').cursor().execute('create table foo (bar text)')
# Test sqlite3.connect(':memory:').cursor().execute('insert into foo (bar) values (?)', ('baz',))
# Test sqlite3.connect(':memory:').cursor().execute('select * from foo where bar=?', ('baz',)).fetchall()

# Test sqlite3.connect(':memory:').cursor().execute('select sqlite_version()').fetchall()
# Test sqlite3.connect(':memory:').cursor().execute('select sqlite_version()').fetchone()
# Test sqlite3.connect(':memory:').cursor().execute('select sqlite_version()').fetchmany()

# Test sqlite3.connect(':memory:').cursor().execute('select sqlite_version()').fetchmany(10)
# Test sqlite3.connect(':memory:').cursor().execute('
