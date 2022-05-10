import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# A global connection object that is reused in multithreaded environment.
conn = None

def worker(n):
  # The sqlite3.connect() will open a second connection (not reused).
  c = sqlite3.connect('test.db')
  global conn
  # Attempt to reuse the global connection object.
  if conn is None:
    conn = c
  else:
    assert conn == c
    c.close()

threads = []
for i in range(5):
  t = threading.Thread(target=worker, args=(i,))
  threads.append(t)
  t.start()

for t in threads:
  t.join()

# Assert that storage is freed if the global connection object
# is closed explicitly (the following close() doesn't work).
# We don't test that since it's ok to leave the storage allocated.
#conn.close()
