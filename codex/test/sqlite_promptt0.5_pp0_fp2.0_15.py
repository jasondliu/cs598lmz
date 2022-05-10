import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/tmp/test.db')
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('file:test.db?mode=memory&cache=shared')
# Test sqlite3.connect('file::memory:?cache=shared')
# Test sqlite3.connect('file::memory:', uri=True)
# Test sqlite3.connect('file:test.db?mode=memory', uri=True)
# Test sqlite3.connect('file::memory:?cache=shared', uri=True)

class Thread(threading.Thread):
    def run(self):
        conn = sqlite3.connect(':memory:')
        conn.execute('create table test(x)')
        for i in range(100):
            conn.execute('insert into test values (?)', (i,))
        conn.commit()
        conn.close()

threads = [Thread() for i in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

