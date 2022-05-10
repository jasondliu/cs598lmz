import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect('test.db')
c = conn.cursor()
print(c)
# c.execute('CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY AUTOINCREMENT, num INTEGER, data TEXT)')
# c.execute('INSERT INTO test(num, data) VALUES(1, "first")')
# c.execute('INSERT INTO test(num, data) VALUES(2, "second")')
# c.execute('INSERT INTO test(num, data) VALUES(3, "third")')
# conn.commit()
c.execute('SELECT * FROM test')
print(c.fetchall())
# c.execute('UPDATE test SET num = 4 WHERE id = 1')
# c.execute('DELETE FROM test WHERE id = 2')
# conn.commit()
c.execute('SELECT * FROM test')
print(c.fetchall())
c.close()
conn.close()
print(ctypes.util.find_library('python3.6m'))

