import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
def test_sqlite3():
	import sqlite3
	conn = sqlite3.connect(':memory:')
	cur = conn.cursor()
	cur.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, value TEXT)")
	cur.execute("INSERT INTO test_table (value) VALUES ('test')")
	for i in range(1,1000): cur.execute("INSERT INTO test_table (id, value) VALUES(?, 'test')", (i,))
	cur.close()
	conn.commit()
	conn.close()
# test_sqlite3()

def test_sqlite3_threading():
	import sqlite3
	import threading
	def doit():
		conn = sqlite3.connect(':memory:')
		cur = conn.cursor()
		cur.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, value TEXT)")
		cur.execute("INSERT INTO test_table (value) VALUES ('test')")
