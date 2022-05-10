import ctypes
import ctypes.util
import threading
import sqlite3

# we need to find the right library
lib = ctypes.util.find_library("libsqlite3")
# initialize it
sqlite3 = ctypes.CDLL(lib)

# initialize vars
db = None
rs = None

def init_db(database):
    global db
    db = sqlite3.sqlite3_open(database, 0)

def query(sql):
    global db
    global rs

    # close old result set
    if not rs is None:
        sqlite3.sqlite3_finalize(rs)

    # prepare new query
    sqlite3.sqlite3_prepare_v2(db, sql, -1, byref(rs), 0)

def get_result():
    global rs
    if sqlite3.sqlite3_step(rs) == sqlite3.SQLITE_ROW:
        # return tuple
        return _get_row()
    return ()

def get_results():
    global rs
    ret = []
    while sqlite3.sqlite3_step(rs)
