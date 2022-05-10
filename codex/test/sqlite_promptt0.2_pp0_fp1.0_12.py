import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# db = sqlite3.connect('test.db')
# cursor = db.cursor()
# cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
# cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'Michael\')')
# print(cursor.rowcount)
# db.commit()
# cursor.close()
# db.close()

# Test sqlite3.Row
# db = sqlite3.connect('test.db')
# cursor = db.cursor()
# cursor.execute('SELECT * FROM user WHERE id=?', ('1',))
# values = cursor.fetchall()
# print(values)
# print(cursor.description)
# for row in values:
#     print(row)
#     print(row[0], row[1])
#     print(row['id'], row['name'])
# cursor.close()
# db.close()

# Test sqlite3.Row
# db = sqlite
