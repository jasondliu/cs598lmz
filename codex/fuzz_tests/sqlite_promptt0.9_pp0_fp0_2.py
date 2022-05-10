import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

def create_memory_table():
    """
    This function creates a table, for storing in memory
    """
    try:
        conn_mem = sqlite3.connect(':memory:')
        cur_mem = conn_mem.cursor()

        # Create table
        cur_mem.execute('''CREATE TABLE if not exists stocks(date text, trans text, symbol text, qty real, price real)''')
        print cur_mem.fetchone()
    except sqlite3.DatabaseError as err:
        print err

    conn_mem.close()

def create_memory_table1():
    """
    This function creates a table, for storing in memory
    """
    try:
        conn_mem = sqlite3.connect(':memory:')
        cur_mem = conn_mem.cursor()

        # Insert a row of data
        cur_mem.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        print cur_mem.fetchone()
    except sqlite
