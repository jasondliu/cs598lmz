import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#cc = sqlite3.connect(':memory:')
# Test sqlite3.Cursor
#cursor = cc.cursor()
# Test cursor.execute
#cursor.execute('CREATE TABLE test(id INTEGER PRIMARY KEY, data TEXT)')
# Test sqlite3.Binary
#if False:
#  cursor.execute('INSERT INTO test(data) VALUES(?)', (sqlite3.Binary(b"hello world")), )
# Test cursor.commit
#cc.commit()
# Test cursor.close
#cursor.close()
# Test connect.close
#cc.close()

# Test sqlite3.Row
#cursor = cc.cursor()
#cursor.execute('SELECT * FROM test')
#for row in cursor:
#    print(row[0], row['data'])

# Test sqlite3.connect(database,timeout,isolation_level,detect_types,factory)
#db = sqlite3.connect('test.db',detect_types=sqlite3.PARSE_DEC
