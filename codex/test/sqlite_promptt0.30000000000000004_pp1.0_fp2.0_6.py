import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# This is a hack to make sure that the shared memory is not freed
# while the test is running.
_keep_alive = []

def _test_thread(db, n):
    cursor = db.cursor()
    cursor.execute('CREATE TABLE test(id INTEGER PRIMARY KEY, value INTEGER)')
    cursor.execute('INSERT INTO test VALUES(1, ?)', (n,))
    cursor.execute('SELECT value FROM test WHERE id=1')
    assert cursor.fetchone()[0] == n
    cursor.close()
    db.commit()

def test_thread():
    db = sqlite3.connect(':memory:', uri=True)
    threads = [threading.Thread(target=_test_thread, args=(db, i))
               for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    db.close()

