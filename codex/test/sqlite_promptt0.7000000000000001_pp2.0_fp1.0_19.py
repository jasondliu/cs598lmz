import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
# Test db.close()
# Test db.cursor()
# Test db.commit()
# Test cur.execute('CREATE TABLE test(id integer primary key, name varchar(32))')
# Test cur.execute('INSERT INTO test VALUES(1, "hello")')
# Test cur.execute('SELECT * FROM test')
# Test cur.fetchone()
# Test cur.execute('DROP TABLE test')

# Test sqlite3.connect_with_lock()
# Test db.lock()
# Test db.unlock()
# Test db.locked()

# Test cur.execute('DELETE FROM test')
# Test cur.executemany('INSERT INTO test VALUES(?, ?)', ((2, 'world'), (3, 'hello world')))
# Test cur.executemany('INSERT INTO test VALUES(?, ?)', ((), ()))
# Test cur.executemany('INSERT INTO test VALUES(?, ?)', ((), (), ()))
# Test cur.executemany('INSERT INTO test VALUES(
