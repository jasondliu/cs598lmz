import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() : SQLite 3.7.15
db = sqlite3.connect('./test.db')
cursor = db.cursor()
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)
# Test sqlite3.Row()
for i in cursor.execute('select * from user where id=?', ('1',)):
    print(i)
    print('Name:%s id:%s' % i)
    print('Name:%s id:%s' % (i[0], i[1]))
    
cursor.close()
db.commit()
db.close()

# Test sqlite3.Row().keys()
cursor = db.cursor()
cursor.execute('select * from user where id=?', ('1',))
#print(cursor.fetchone())
