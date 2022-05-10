import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
dbfilename = 'db1.sqlite3'
conn = sqlite3.connect(dbfilename)
print(conn)

# :memory: is kept in the RAM
conn = sqlite3.connect(':memory:')
print(conn)

# open database
dbfilename = 'db1.sqlite3'
conn = sqlite3.connect(dbfilename)
curs = conn.cursor()
curs.execute('''CREATE TABLE book(
id INTEGER PRIMARY KEY,
title TEXT,
author TEXT,
published INTEGER)''')

# insert data
curs.execute('''INSERT INTO book(title, author, published)
VALUES('Dive into Python', 'Mark Pilgrim', 2003)''')

data = [('High Performance Python', 'Ian Ozsvald', 2009),
('Programming Collective Intelligence', 'Toby Segaran', 2007),
('Head First Python', 'Paul Barry', 2009)]
for row in data:
    query = 'INSERT INTO book(title, author, published) VALUES(?, ?, ?)'
   
