import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# Test sqlite3.connect(":memory:")

def sqlite_connect(memdb=None):
    global conn
    global cur
    if memdb is None:
        conn = sqlite3.connect('test.db')
        cur  = conn.cursor()
    else:
        conn = sqlite3.connect(':memory:')
        cur  = conn.cursor()

    return conn, cur

def init_db():
    sql_create_table = """CREATE TABLE IF NOT EXISTS dashboard (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        timestamp DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP,'LOCALTIME')),
                                        time_stamp_ms VARCHAR(100),
                                        device_id VARCHAR(100),
                                        temperature VARCHAR(100),
                                        humidity VARCHAR(100),
                                        pressure VARCHAR(100),
                                        brightness VARCHAR(100),
                                        status VARCHAR(100)
