import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(':memory:')
# Test sqlite3.Cursor.execute()
c = conn.cursor()
c.execute('SELECT SQLITE_VERSION()')
# Test sqlite3.Cursor.fetchall()
print(c.fetchall())
# Test sqlite3.Cursor.close()
c.close()
# Test sqlite3.Connection.close()
conn.close()
# Test sqlite3.Connection.commit()
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE test(id integer primary key, text)')
c.execute('INSERT INTO test (text) VALUES ("foobar")')
conn.commit()
c.execute('SELECT * FROM test')
print(c.fetchall())
conn.close()

# test sqlite3.Connection.rollback()
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE test(id integer primary key, text)')
