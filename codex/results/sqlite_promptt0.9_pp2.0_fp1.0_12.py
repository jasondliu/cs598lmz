import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections.row
from _sqlite3 import *


class DBAPI(object):
    ThreadingConnection = None
    def setup_class(cls):
        import sqlite3
        sa = sqlite3.ensure_bytes(':memory:')
        cls.cpython_connections = [
            sqlite3.connect(sa),
            sqlite3.connect(sa),
            sqlite3.connect(sa),
        ]
        cls.ThreadingConnection = type(cls.cpython_connections[0])

    def teardown_class(cls):
        while cls.cpython_connections:
            conn = cls.cpython_connections.pop()
            conn.close()
        cls.cpython_connections = None


# XXX: This class should inherit from the DBAPI plugin
class Test_sqlite3_cursors(object):
    # For backwards compatibility, the C extension module still needs to be
    # imported in the default namespace, at least for the time being.
    from _sqlite3 import connection, cursor, Warning
