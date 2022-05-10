import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

db_file_path = "data.db"
db_url = "sqlite:///" + db_file_path

con = sqlite3.connect(db_file_path)

assert con._is_connection_closed


# Test sqlite3.connect() with param
def test_connect_with_param():
    con = sqlite3.connect(db_file_path, uri=True)

    assert con._is_connection_closed

def test_threadsafety():
    assert sqlite3.threadsafety == sqlite3.PARTHREAD == 1
    assert sqlite3.sqlite_version == '3.7.7'
    assert sqlite3.paramstyle == 'qmark'
    assert sqlite3.version == '1.0.1'

def test_connect_filename():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("select 4+5")
    assert cur.fetchone() == (9,)

def test_connect_urifilename():
   
