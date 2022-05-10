import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
import time

class Sqlite3Test(unittest.TestCase):
    def test_sqlite3_db_init(self):
        db = sqlite3.connect('test.db')
        self.assertNotEqual(db, None)
        db.close()

    def test_sqlite3_table_init(self):
        db = sqlite3.connect('test.db')
        cursor = db.cursor()
        cursor.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, text VARCHAR(20))')
        db.close()

    def test_sqlite3_insert_and_select(self):
        db = sqlite3.connect('test.db')
        cursor = db.cursor()
        cursor.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, text VARCHAR(20))')
        cursor.execute('INSERT INTO test (text) VALUES (?)', ('test',))
        cursor.execute('SELECT * FROM test')
        self.assertEqual(cursor
