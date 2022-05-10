import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() by creating a database in memory and checking that a
# table created in one thread is accessible from another thread.  This
# verifies that the database connection is being properly shared between
# threads.

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

libc.sigwait.restype = ctypes.c_int
libc.sigwait.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_void_p))

def worker(con):
    con.execute("create table test(id, name)")
    libc.sigwait(ctypes.byref(ctypes.c_int(signal.SIGUSR1)), None)
    con.execute("insert into test(id, name) values (1, 'foo')")

def checker(con):
    con.execute("select * from test")
    row = con.fetchone()
