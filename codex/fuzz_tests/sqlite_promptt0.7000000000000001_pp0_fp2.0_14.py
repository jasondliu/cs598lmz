import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(':memory:')
c = conn.cursor()
# Test sqlite3.complete_statement()
print(sqlite3.complete_statement('SELECT * FROM t1;'))
print(sqlite3.complete_statement('SELECT * FROM t1'))
print(sqlite3.complete_statement('SELECT * FROM t1\n'))
print(sqlite3.complete_statement('SELECT * FROM t1\nGO'))
# Test sqlite3.enable_callback_tracebacks()
sqlite3.enable_callback_tracebacks(True)
# Test sqlite3.connect()
conn = sqlite3.connect('test.db')
# Test sqlite3.Connection
print(conn.isolation_level)
conn.create_function('pow', 2, pow)
conn.execute('CREATE TABLE t1(x,y)')
c = conn.cursor()
c.execute('INSERT INTO t1 (x,y) VALUES(?,?)', (3,4))
c.execute('SELECT pow(?,?)', (
