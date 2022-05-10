import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and sqlite3.close
assert(sqlite3.connect(':memory:'))
assert(sqlite3.connect('test') == False)
assert(sqlite3.connect('/test') == False)

conn = sqlite3.connect(':memory:')
assert(conn)
assert(isinstance(conn, sqlite3.Connection))
assert(conn.isolation_level == None)
conn = sqlite3.connect(':memory:', isolation_level = None)
conn.close()
assert(conn.isolation_level == None)

conn = sqlite3.connect(':memory:', isolation_level = '')
conn.close()
assert(conn.isolation_level == '')

conn = sqlite3.connect(':memory:', isolation_level = 'DEFERRED')
conn.close()
assert(conn.isolation_level == 'DEFERRED')

conn = sqlite3.connect(':memory:', isolation_level = 'IMMEDIATE')
conn.close()
assert(conn.isolation_level == 'IMMEDIATE')

