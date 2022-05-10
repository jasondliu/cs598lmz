import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('CREATE TABLE foo (bar STRING)')
cur.execute('INSERT INTO foo (bar) VALUES (?)', ('baz',))
cur.execute('SELECT bar FROM foo')
print(cur.fetchone()[0])
# Test sqlite3.connect() with autocommit = True
conn = sqlite3.connect(':memory:', isolation_level=None)
cur = conn.cursor()
cur.execute('CREATE TABLE foo (bar STRING)')
cur.execute('INSERT INTO foo (bar) VALUES (?)', ('baz',))
cur.execute('SELECT bar FROM foo')
print(cur.fetchone()[0])

# Test Interrupt
# This test requires the use of a thread.
def start_thread():
    try:
        threading.Thread(target=conn.cursor().execute,
                         args=('SELECT * FROM foo',), kwargs={}).start()
        time.sleep(.1)

