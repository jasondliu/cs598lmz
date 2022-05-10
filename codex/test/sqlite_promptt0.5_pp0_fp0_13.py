import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
class sqlite3_connect(threading.Thread):
    def run(self):
        try:
            conn = sqlite3.connect(':memory:')
            cursor = conn.cursor()
            cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
            cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
            print(cursor.rowcount)
            cursor.close()
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

# Test sqlite3.cursor
