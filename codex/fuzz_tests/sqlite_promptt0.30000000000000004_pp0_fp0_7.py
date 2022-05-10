import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

def _sqlite_connect(db_path):
    """
    Connect to a sqlite database.
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print("Error %s:" % e.args[0])
        return None


def _sqlite_disconnect(conn):
    """
    Disconnect from a sqlite database.
    """
    try:
        conn.close()
    except sqlite3.Error as e:
        print("Error %s:" % e.args[0])


def _sqlite_execute(conn, sql):
    """
    Execute a sqlite query.
    """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return cur
    except sqlite3.Error as e:
        print("Error %s:" % e.args[0])
        return None


def _sqlite_executemany(conn, sql, values):
    """
   
