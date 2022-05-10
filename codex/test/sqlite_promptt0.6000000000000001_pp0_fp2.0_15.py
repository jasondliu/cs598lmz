import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
# Test sqlite3.Connection
conn.execute('select 1')
# Test sqlite3.Cursor
cursor = conn.cursor()
cursor.execute('select 1')
# Test sqlite3.Row
row = cursor.fetchone()
row[0]

# Test sqlite3.Connection.commit
conn.commit()
# Test sqlite3.Connection.rollback
conn.rollback()
# Test sqlite3.Connection.close
conn.close()

# Test sqlite3.register_converter
def converter(value):
    return value
conn = sqlite3.connect(':memory:')
conn.execute("create table test(data)")
conn.execute("insert into test(data) values (?)", (1,))
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("select data from test")
row = cursor.fetchone()
row['data']
conn.register_converter("test", converter)
conn
