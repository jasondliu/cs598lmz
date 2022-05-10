import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
def test_conn():
	conn = sqlite3.connect(':memory:')
	cur = conn.cursor()
	cur.execute('CREATE TABLE cache_record (chunkid TEXT NOT NULL, \
										   whence INT NOT NULL, \
										   len INT NOT NULL, \
										   offset INT NOT NULL, \
										   PRIMARY KEY (chunkid, whence))')
	for i in xrange(1, 4):
		cur.execute("INSERT INTO cache_record VALUES ('chunk_id_%d', '%d', '%d', '%d')" % (i, i+1, i+5, i+10))
	conn.commit()
	conn.close()

# This class is responsible for caching
class LRU():
	def __init__(self, chunk_size, capacity):
		self.chunk_size = chunk_size
		self.capacity
