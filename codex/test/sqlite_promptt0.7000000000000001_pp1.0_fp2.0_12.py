import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

def main():
    f = 'sqlite3.db'
    conn = sqlite3.connect(f)
    c = conn.cursor()
    c.execute('select * from bbb')
    rs = c.fetchall()
