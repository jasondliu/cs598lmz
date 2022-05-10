import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

#
# 1. Create a SQLite database in memory.
#

db = sqlite3.connect(':memory:')
db.isolation_level = None

#
# 2. Create a table and add some data.
#

db.execute('create table numbers (i)')
db.execute('insert into numbers values (1)')
db.execute('insert into numbers values (2)')
db.execute('insert into numbers values (3)')
db.execute('insert into numbers values (4)')

#
# 3. Change it to a column-oriented database.
#

db.execute('pragma page_size=0')
db.execute('create table number1 (i)')
db.execute('insert into number1 select i from numbers')
db.execute('drop table numbers')
db.execute('alter table number1 rename to numbers')

#
# 4. Create a table with a single row.
#

db.execute('create table one (i)')
db.execute('insert into one values (1)')

#
