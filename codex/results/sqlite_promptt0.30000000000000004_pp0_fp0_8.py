import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()

def test_connect():
    db = sqlite3.connect(':memory:')
    assert db.execute('select 1').fetchone()[0] == 1

def test_connect_with_uri():
    db = sqlite3.connect('file:test?mode=memory&cache=shared')
    assert db.execute('select 1').fetchone()[0] == 1

def test_connect_with_uri_filename_only():
    db = sqlite3.connect('test?mode=memory&cache=shared')
    assert db.execute('select 1').fetchone()[0] == 1

def test_connect_with_uri_filename_only_schemeless():
    db = sqlite3.connect('test')
    assert db.execute('select 1').fetchone()[0] == 1

def test_connect_with_uri_schemeless():
    db = sqlite3.connect('file:test')
    assert db.execute('select 1').fetchone()[0] == 1
