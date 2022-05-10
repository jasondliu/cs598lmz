import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection
# type the following in interactive console:
# import sqlite3
# sqlite3.sqlite3.Parse
# <built-in method Parse of sqlite3.Cursor object at 0x00000000020E4040>

# conn = sqlite3.connect(':memory:')
# print type(conn)
# <class 'sqlite3.Connection'>


# conn.execute('create table users (user_id int primary key, username varchar(40))')
# conn.executemany('insert into users (user_id, username) values (?, ?)', [(1, 'admin'), (2, 'user')])
# conn.commit()
# for row in conn.execute('select * from users'):
#     print row



class SQLiteDAO(threading.Thread):
    def __init__(self, command_queue, connect_name='app.sqlite', logger=None):
        super(SQLiteDAO, self).__init__()
        self.daemon = True
        self.command_queue = command_queue
        self.logger
