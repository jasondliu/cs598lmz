import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() without specifying a database file.
# This will connect to a new, temporary database.
con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('create table abc (id integer primary key, name text)')
cur.execute('insert into abc (name) values (?)', ('foo',))
cur.execute('insert into abc (name) values (?)', ('bar',))
cur.execute('insert into abc (name) values (?)', ('baz',))
cur.execute('select * from abc')
print(cur.fetchall())
con.close()

# In the above example, we only used the most basic features of the
# Python sqlite3 module to query our database. SQLite in fact has
# many more features; to learn more about them, see the SQLite
# documentation at http://www.sqlite.org/.
#
# Now we will look at how to use the Python sqlite3 module in a
# more advanced way. As a first example, we will use it to connect
# to an existing database file.


