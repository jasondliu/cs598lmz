import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('dbs/hello.db').execute('create table test_table')

# I got an exception(no such table) when I tried to insert records into a database with a table
# in a separate thread.
# It turns out the database lock was not released by the database connection object before the thread
# exits.
# For example, this code won't work, because the db object is not released before the thread exits:

# import threading, sqlite3
# def test_threading(lock):
#     db = sqlite3.connect('dbs/hello.db')
#     cur = db.cursor()
#     cur.execute('create table test_table')
#     cur.execute('insert into test_table (id, name) values (1, "name1")')
#     db.commit()
#     print 'thread exits'
#     lock.release()
# lock = threading.Lock()
# lock.acquire()
# thread = threading.Thread(target=test_threading, args=(lock, ))
# thread.start()
# lock.acquire()
# lock
