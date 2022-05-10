import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess

def init_db():
    try:
        os.remove("test.db")
    except:
        pass
    db = sqlite3.connect("test.db")
    db.execute("create table t1(c1 INTEGER, c2 REAL, c3 TEXT)")
    db.commit()
    return db

def close_db(db):
    db.close()

def testcase(db):
    print("testcase ----------------------------------------------")
    db.execute("insert into t1 values (1, 1.1, 'hello world')")
    db.execute("insert into t1 values (2, 2.2, 'hello world')")
    db.execute("insert into t1 values (3, 3.3, 'hello world')")
    db.execute("insert into t1 values (4, 4.4, 'hello world')")
    db.execute("insert into t1 values (5, 5.5, 'hello world')")
