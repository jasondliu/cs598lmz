import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
db = sqlite3.connect('libs.db')
db.execute('CREATE TABLE LIB(NAME CHAR(100) PRIMARY KEY NOT NULL, LIBHANDLE POINTER)')
# It's safe to call sqlite3.connect() everytime
# Just don't call sqlite3.connect() inside another sqlite3.connect() call.
db.execute('INSERT INTO LIB(NAME,LIBHANDLE) VALUES(?,?)',('test_lib',0))
db.commit()
db.close()
# Test sqlite3.connect()
db = sqlite3.connect('libs.db')
db.execute('CREATE TABLE LIB(NAME CHAR(100) PRIMARY KEY NOT NULL, LIBHANDLE POINTER)')
# It's safe to call sqlite3.connect() everytime
# Just don't call sqlite3.connect() inside another sqlite3.connect() call.
db.execute('INSERT INTO LIB(NAME,LIBHANDLE) VALUES(?,?)',('test_lib',0))
db.commit()
db.close()
# Test
