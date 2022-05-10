import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with the following argument
import os
import sys
import time


def _connect(filename):
    return sqlite3.connect(
        filename,
        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        check_same_thread=False
    )

db = _connect(
    os.path.join(sys.path[0], 'data/data.db')
)


def execute(sql, params=None):
    try:
        if params is None:
            db.execute(sql)
        else:
            db.execute(sql, params)
        db.commit()
    except:
        db.rollback()
        raise


def executemany(sql, params):
    try:
        db.executemany(sql, params)
        db.commit()
    except:
        db.rollback()
        raise


def executescript(sql):
    try:
        db.executescript(sql)
        db.commit()
    except:
        db.roll
