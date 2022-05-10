import ctypes
import ctypes.util
import threading
import sqlite3
import time

# print(ctypes.util.find_library('pthread'))
libpthread = ctypes.CDLL(ctypes.util.find_library('pthread'))

def make_cancel_thread(cursor):
    c = cursor

    def cancel_thread():
        print("starting cancel thread")
        time.sleep(3)
        # Issue a cancel query
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.get_ident()), ctypes.py_object(sqlite3.OperationalError))
        print("cancelled query")
    return cancel_thread


def main():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE stuff(id int primary key, value int);")
    conn.execute("INSERT INTO stuff VALUES (1, 1234);")
    conn.execute("INSERT INTO stuff VALUES (2, 5678);")
    conn.execute("INSERT INTO stuff VALUES (3, 9012);")
    conn.commit
