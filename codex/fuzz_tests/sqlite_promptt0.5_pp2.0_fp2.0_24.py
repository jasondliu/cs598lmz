import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

def sqlite_connect(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def sqlite_create_table(conn, table_name):
    sql = '''create table %s (
            id integer primary key autoincrement,
            name text not null,
            age integer not null
            )''' % (table_name)
    conn.execute(sql)
    conn.commit()

def sqlite_insert_data(conn, table_name):
    sql = "insert into %s (name, age) values ('%s', %d)" % (table_name, 'Tom', 20)
    conn.execute(sql)
    conn.commit()

def sqlite_query_data(conn, table_name):
    sql = "select * from %s" % (table_name)
    cursor = conn.execute(sql)
    for row in cursor:
        print(row)

def sqlite_close(conn):
    conn.close()

def test_sqlite():
    db_name = '
