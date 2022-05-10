import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() in Python interactive mode
>>> sqlite3.connect('test.db')
# In Python, you can also use sqlite3.connect() in program

# create table in SQLite
CREATE TABLE stocks
  (date text, trans text, symbol text, qty real, price real)
# insert rows in SQLite
INSERT INTO stocks
  VALUES ('2006-01-05', 'BUY', 'RHAT', '100', '35.15')
INSERT INTO stocks VALUES ('2006-01-10', 'SELL', 'RHAT', '100', '35.14')

# select data in SQLite
SELECT * FROM stocks

# delete rows in SQLite
DELETE FROM Stocks WHERE Symbol='RHAT'

# prepare SQLite command and execute command
from sqlite3 import connect
conn = sqlite3.connect('test.db')
curs = conn.cursor()
#curs.execute('CREATE TABLE dessert (NAME, WEIGHT, PRICE)') '''
curs.execute('DROP TABLE dessert')
curs.execute('CREATE TABLE dessert (NAME v
