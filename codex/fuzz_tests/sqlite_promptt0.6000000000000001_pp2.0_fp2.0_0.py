import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
# Test sqlite3.connect('file:memory:?cache=private')
# Test sqlite3.connect('file:memory:?cache=shared')
# Test sqlite3.connect('file:memory:?cache=private')

def test_cache_shared():
    """
    Test sqlite3.connect('file:memory:?cache=shared')
    """
    con1 = sqlite3.connect('file:memory:?cache=shared')
    con2 = sqlite3.connect('file:memory:?cache=shared')

    cur1 = con1.cursor()
    cur1.execute('CREATE TABLE test(x)')

    cur2 = con2.cursor()
    cur2.execute('SELECT name FROM sqlite_master WHERE type="table"')
    assert cur2.fetchone()[0] == 'test'

    cur1.execute('DROP TABLE test')

    cur2 = con2.cursor()
    cur2.execute('SELECT name FROM sqlite_master WHERE type="table"')

