import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE foo (bar text)')
c.execute("INSERT INTO foo (bar) VALUES ('baz')")
c.execute('SELECT * FROM foo')
row = c.fetchone()
assert row[0] == 'baz'
# Test ctypes.util.find_library
libc_path = ctypes.util.find_library('c')
assert libc_path
# Test threading.Lock
lock = threading.Lock()
lock.acquire()
lock.release()
# Test ctypes.CDLL
libc = ctypes.CDLL(libc_path)
libc.printf(b"Hello, %s!\n", b"world")
# Test os.listdir
assert os.listdir(os.getcwd())
# Test os.getcwd
assert os.getcwd()
# Test os.path.isfile
assert os.path.isfile(__file__)
# Test os.path.exists

