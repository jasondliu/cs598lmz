import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def test_connect():
    conn = sqlite3.connect(':memory:') # Empty DB
    conn.close()

def test_connect_in_thread():
    def _connect():
        conn = sqlite3.connect(':memory:') # Empty DB
        conn.close()

    t = threading.Thread(target=_connect)
    t.start()
    t.join()

def test_connect_in_process():
    class Connect(multiprocessing.Process):
        def run(self):
            conn = sqlite3.connect(':memory:') # Empty DB
            conn.close()

    p = Connect()
    p.start()
    p.join()

def test_connect_with_timeout():
    conn = sqlite3.connect(':memory:', timeout=0.1) # Empty DB
    conn.close()

def test_connect_with_timeout_in_thread():
    def _connect():
        conn = sqlite3.connect(':memory:', timeout=0.1) # Empty DB
       
