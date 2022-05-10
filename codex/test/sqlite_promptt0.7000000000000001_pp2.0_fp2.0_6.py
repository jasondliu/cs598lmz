import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect function
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
print(cursor.execute('pragma database_list').fetchall())
cursor.execute('create table test (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into test (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)
cursor.close()
conn.commit()
cursor = conn.cursor()
cursor.execute('select * from test where id=?', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

# Test sqlite3.cursor function
def test(conn):
    # cursor = conn.cursor()
    cursor = conn.cursor(cursor=sqlite3.Cursor)
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20), score int)')
