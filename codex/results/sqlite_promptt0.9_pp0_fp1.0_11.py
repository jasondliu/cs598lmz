import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect


def ins(db, atr1, atr2, atr3):
    cu = db.cursor()
    try:
        r = cu.execute('INSERT INTO test(00,01,02) VALUES(?,?,?)', (atr1, atr2, atr3))
        r = db.commit()
        print r
    except Exception, e:
        print e

def sel(db):
    cu = db.cursor()
    r = cu.execute('SELECT * from test')
    r = cu.fetchall()
    for i in r:
        print '%d,%d,%d' % (i[0], i[1], i[2])

def init(db):
    cu = db.cursor()
    cu.execute('PRAGMA auto_vacuum = full')
    cu.execute('CREATE TABLE test (id int primary key, 00 int, 01 int, 02 int)')
    cu.execute('CREATE INDEX key00 ON test(00)')
    cu.execute('CREATE INDEX
