import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name VARCHAR(10))')
cursor.execute('INSERT INTO test VALUES (1, "foo")')
cursor.execute('INSERT INTO test VALUES (2, "bar")')
cursor.execute('SELECT * FROM test')
print cursor.fetchall()
# Test ctypes.util.find_library
print ctypes.util.find_library('c')
# Test ctypes.CDLL
libc = ctypes.CDLL(ctypes.util.find_library('c'))
print libc.printf('Hello %s!\n', 'World')
# Test threading.Thread
def hello():
    print 'Hello World!'
thread = threading.Thread(target=hello)
thread.start()
thread.join()
