import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() the way it is called in real life
with sqlite3.connect(":memory:") as con1:
    assert isinstance(con1, sqlite3.Connection)
    # Test sqlite3.connect() taking bytes as sqlite_file arguments
    with sqlite3.connect(b":memory:") as con2:
        assert isinstance(con2, sqlite3.Connection)
        # Check that cursor() and executescript() are present in the real life case
        assert isinstance(con2.cursor(), sqlite3.Cursor)
        con2.executescript("select 1;")
        # Test that multiple connection can be opened at a time
        with con2:
            assert isinstance(con2, sqlite3.Connection)
            assert isinstance(con2.cursor(), sqlite3.Cursor)
    # Check that cursor() and executescript() are present in the other case
    assert isinstance(con1.cursor(), sqlite3.Cursor)
    con1.executescript("select 1;")


class Namespace(object):
    pass


