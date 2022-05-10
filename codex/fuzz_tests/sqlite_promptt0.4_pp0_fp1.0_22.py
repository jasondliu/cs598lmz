import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with a URI
#
# The test is run in a separate process, because it may call exit()
# and we want to avoid that.

# This is the URI we will use
URI = 'file:test.db?mode=rwc'

# Create a database, and put some data in it
db = sqlite3.connect(URI)
cur = db.cursor()
cur.execute('create table test(x, y)')
cur.execute('insert into test(x, y) values(?, ?)', (1, 2))
cur.execute('insert into test(x, y) values(?, ?)', (3, 4))
db.commit()

# Now, open a new connection to the same database
db2 = sqlite3.connect(URI)
cur2 = db2.cursor()

# Check that the data is there
cur2.execute('select x, y from test')
for row in cur2:
    print(row)

# Check that the data is still there
cur.execute('select x, y from test')
for row in cur:
    print
