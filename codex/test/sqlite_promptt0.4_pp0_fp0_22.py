import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

db_path = "./test.db"

def create_table():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE test_table (id integer primary key, data text)")
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO test_table(data) VALUES ('test1')")
    c.execute("INSERT INTO test_table(data) VALUES ('test2')")
    c.execute("INSERT INTO test_table(data) VALUES ('test3')")
    conn.commit()
    conn.close()

def select_data():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    cursor = c.execute("SELECT * FROM test_table")
    for row in cursor:
        print(row)
    conn.close()

