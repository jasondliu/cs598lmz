import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

name = 'test1.db'

# Open or create a database file.
conn = sqlite3.connect(name)

# Get the cursor to execute sql.
cur = conn.cursor()

# Drop a table.
if True:
    cur.execute('drop table test')

# Create a table.
if True:
    cur.execute('''create table test (id integer, profit integer, type text)''')

# Insert data.
if True:
    cur.execute('''insert into test values (1, 20, 'foo bar')''')
    cur.execute('''insert into test values (2, 10, 'a b')''')
    cur.execute('''insert into test values (3, 50, 'goq')''')

# Commit.
if True:
    conn.commit()

# Select.
if True:
    for row in cur.execute('select * from test'):
        print(row)


conn.close()

