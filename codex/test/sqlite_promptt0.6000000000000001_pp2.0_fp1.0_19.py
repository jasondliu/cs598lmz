import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, str TEXT)')
db.execute('INSERT INTO test (str) VALUES (:str)', {'str': 'test'})
db.commit()
print(db.execute('SELECT str FROM test').fetchone()[0])

# Test ctypes.CDLL
lib = ctypes.CDLL(ctypes.util.find_library('c'))
lib.puts(b'test')

# Test threading.Thread
def f(x):
    for _ in range(10):
        print(x)

threading.Thread(target=f, args=(1,)).start()
threading.Thread(target=f, args=(2,)).start()
