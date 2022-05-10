import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

_libc = ctypes.CDLL(ctypes.util.find_library("c"))
_clock = _libc.clock
_clock.restype = ctypes.c_long

class Timer(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def start(self):
        self.begin = _clock()

    def stop(self):
        self.end = _clock()

    def elapsed(self):
        return (self.end - self.begin) / 1000.0

def test(n):
    timer = Timer()
    conn = sqlite3.connect(":memory:")
    timer.start()
    for i in range(n):
        conn.execute("create table t(i)")
    timer.stop()
    print("create table: %.3f ms" % (timer.elapsed() * 1000))

    timer.start()
    for i in range(n):
        conn.execute("insert into t(i) values (?)", (i,
