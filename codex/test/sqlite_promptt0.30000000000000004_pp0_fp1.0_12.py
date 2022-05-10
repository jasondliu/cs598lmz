import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared")

class _SQLiteSharedCache(object):
    def __init__(self, db_name):
        self.db_name = db_name
        self.lock = threading.Lock()
        self.connections = []
        self.connections_lock = threading.Lock()
        self.sqlite_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.sqlite_lib.sqlite3_enable_shared_cache(1)

    def get_connection(self):
        with self.lock:
            conn = sqlite3.connect(self.db_name)
            with self.connections_lock:
                self.connections.append(conn)
            return conn

    def close_connections(self):
        with self.connections_lock:
            for conn in self.connections:
                conn.close()
            self.connections = []

_shared_cache = {}

