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

def my_cb2(p):
    if hasattr(my_threading_local, "a"):
        del my_threading_local.a
    return 1

def sqlite3_open(filename, flags):
    a = sqlite3.connect(filename, uri=True, factory=deleting_conn)
    a.set_progress_handler(my_cb, 1)
    a.set_trace_callback(my_cb2)
    return a

def sqlite3_close(connection):
    if hasattr(my_threading_local, "a"):
        del my_threading_local.a
    connection.close()

def sqlite3_exec(connection, query):
    connection.execute(query)

def sqlite3_step(statement):
    return statement.step()

def sqlite3_column_blob(statement, column):
    return statement.get_blob(column)

def sqlite3_finalize(statement):
    statement.finalize()

def sqlite3_reset(
