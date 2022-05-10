import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(:memory:)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("create table t(a, b)")
cursor.execute("insert into t(a, b) values (?, ?)", (10, 20))
cursor.execute("insert into t(a, b) values (?, ?)", (30, 40))
cursor.execute("select a from t where b = 40")
print(cursor.fetchone())  # => 30
cursor.execute("select * from t")
print(cursor.fetchall())  # => [10, 20], [30, 40]
conn.close()
print('----------')
# Test sqlite3.connect(/path/to/database.db)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute("select * from t")
print(cursor.fetchall())
conn.close()
print('----------')
# Test sqlite3.connect(/path/to/database.db) and use some external sql
