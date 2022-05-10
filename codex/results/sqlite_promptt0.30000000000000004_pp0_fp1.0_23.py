import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE test (id int, name text)')
c.execute('INSERT INTO test VALUES (1, "hello")')
c.execute('INSERT INTO test VALUES (2, "world")')
c.execute('SELECT * FROM test')
print(c.fetchall())
conn.close()

# Test ctypes
libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.printf(b'Hello, world!\n')

# Test threading
def worker():
    print(threading.current_thread().name)

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
for t in threads:
    t.join()
