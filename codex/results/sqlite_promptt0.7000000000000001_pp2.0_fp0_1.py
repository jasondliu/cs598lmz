import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections

def test_connection():
    #
    # test thread safety of connections.
    # as long as 'conn' is not shared across threads, things are safe.
    #
    conn = sqlite3.connect(':memory:')
    print(conn.execute('pragma integrity_check').fetchone()[0])
    try:
        numthreads = 100
        threads = [threading.Thread(target=lambda: conn.execute('pragma integrity_check').fetchone()[0]) for i in range(numthreads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    finally:
        conn.close()

def test_connection_memory():
    #
    # test thread safety of in-memory databases.
    # this is not safe, since pysqlite handles the :memory: database as a singleton
    #
    conn = sqlite3.connect(':memory:')
    print(conn.execute('pragma integrity_check').fetchone()[0])
    try
