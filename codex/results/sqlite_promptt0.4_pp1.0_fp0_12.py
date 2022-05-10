import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def main():
    conn = sqlite3.connect('/tmp/test.db')
    conn.close()

if __name__ == '__main__':
    main()
