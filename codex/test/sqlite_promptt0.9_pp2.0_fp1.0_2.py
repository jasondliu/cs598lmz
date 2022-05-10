import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.execute()
def sqlite_test():
    # connect to sqlite
    conn = sqlite3.connect(':memory:')
    print(conn)
    c = conn.cursor()
    # insert some value into database
    c.execute('''create table stocks
                 (date text, trans text, symbol text, qty real, price real)''')
    # test 'c.execute' function
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    conn.commit()
    # select
    c.execute('SELECT * FROM stocks')
    stock = c.fetchall()
    print(stock)
    return 1

# Test ctypes.get_errno
def errno_test(is_raise=True):
    if is_raise:
        if errno.errorcode[ctypes.get_errno()] == 'ENOENT':
            raise OSError('Cannot open file')
            print('errno test 2')
