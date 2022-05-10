import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# TODO: move this to a library

def find_lib(name):
    paths = [
        ctypes.util.find_library(name),
        os.path.join(os.path.dirname(__file__), 'lib' + name + '.so'),
        os.path.join(os.path.dirname(__file__), 'lib' + name + '.dylib'),
        os.path.join(os.path.dirname(__file__), 'lib' + name + '.dll'),
    ]
    for p in paths:
        if p:
            return p
    raise Exception("Couldn't find library '%s'" % name)

lib = ctypes.CDLL(find_lib("_cffi_backend"), use_errno=True)

# /TODO

def test_sqlite3_connect(lib):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("create table tt(id int)")
    cur.execute
