import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
import sys
import os
import time

libc = ctypes.CDLL(ctypes.util.find_library('c'))

def test_create(db):
    db.execute('CREATE TABLE test(i)')

def test_insert(db):
    db.execute('INSERT INTO test VALUES (1)')

def test_select(db):
    db.execute('SELECT * FROM test')

def test_update(db):
    db.execute('UPDATE test SET i = i + 1')

def test_delete(db):
    db.execute('DELETE FROM test')

def test_drop(db):
    db.execute('DROP TABLE test')

tests = [test_create, test_insert, test_select, test_update, test_delete, test_drop]

class TestThread(threading.Thread):
    def __init__(self, db, tests):
        threading.Thread.__init__(self)
        self.db = db
        self.tests = tests
