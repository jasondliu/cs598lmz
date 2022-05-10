import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# db = sqlite3.connect('test.db')
# cursor = db.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# print(cursor.rowcount)
# cursor.close()
# db.commit()
# db.close()

# Test sqlite3.Row
# db = sqlite3.connect('test.db')
# cursor = db.cursor()
# cursor.execute('select * from user where id=?', ('1',))
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
# db = sqlite3.connect('test.
