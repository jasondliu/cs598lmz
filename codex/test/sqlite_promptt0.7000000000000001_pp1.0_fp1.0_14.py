import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with a URI.

liburi = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

class Error(Exception): pass

def open_uri(uri, *args):
    db = sqlite3.connect(uri, *args)
    return db

def do_test(name, *args):
    print('Testing {}...'.format(name))
    try:
        open_uri(name, *args)
    except sqlite3.Error as e:
        print('sqlite3.Error: {}'.format(e))
    except OSError as e:
        print('OSError: {}'.format(e))
    except Error as e:
        print('Error: {}'.format(e))

do_test('foo.db')
do_test('file:foo.db?mode=rw', sqlite3.OPEN_URI)
do_test('file:foo.db?mode=rw', sqlite3.OPEN_CREATE | sqlite3.OPEN_URI)
