import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def my_step(p, a, b, c):
    return 1

def my_final(p):
    my_threading_local.a.close()
    return 1

def my_value(p):
    return 1

def my_aggregate_count_step(p, x):
    return 1

def my_aggregate_count_final(p):
    return 1

def my_aggregate_sum_step(p, x):
    return 1

def my_aggregate_sum_final(p):
    return 1

def my_aggregate_avg_step(p, x):
    return 1

def my_aggregate_avg_final(p):
    return 1

def my_aggregate_variance_step(p, x):
    return 1

def my_aggregate_variance_final(p):
    return 1

def my_aggregate_stddev_step(p, x):
    return 1

def my_aggregate_stddev_final(p):
    return
