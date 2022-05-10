import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
def testSqlite3Connect(path):
    return sqlite3.connect(path)
# Test sqlite3.connect_withTimeout
def testSqlite3ConnectWithTimeout(path, ms):
    return sqlite3.connect(path,None,None,None,ms)
# Test sqlite3.connect_withTimeout
def testSqlite3Library():
    return sqlite3.sqlite_version
# Test sqlite3.connect_withTimeout
def testSqlite3LibraryString():
    return sqlite3.sqlite_version_info

def testSqlite3LibraryNumber():
    return sqlite3.version
def testSqlite3LibraryTimeStamp():
    return sqlite3.timeStamp()
def testSqlite3ThreadSafe():
    return sqlite3.threadsafety
    
def testSqlite3ThreadSafetyNumber():
    return sqlite3.threadsafety
# Test sqlite3.connect_withTimeout

def testSqlite3_enable_shared_cache():
    if sqlite3.threadsafety == 1:
       
