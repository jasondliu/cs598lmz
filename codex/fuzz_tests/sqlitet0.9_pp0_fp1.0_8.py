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

# The problem depends on:
#    - the fact that the SQLite connection is a custom type
#      (though it cannot be a subclass of Connection)
#    - the fact that SQLite is used in a threading environment
#    - the fact that the shared library is not loaded immediately
#      after Python gets initialized
#    - the fact that the shared library is explicitly loaded by
#      ctypes.util.find_library
if __name__ == '__main__':
    cd = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
    for i in range(2):
        thread = threading.Thread(target=cd.pthread_create,
                                  args=(ctypes.c_void_p(), ctypes.c_void_p(),
                                        my_cb, ctypes.c_void_p()))
        thread.start()
        thread.join()

# Copyright (C) 2013 Victor Stinner <victor.stinner AT gmail.com>
#
# This file is part of python-pysqlite.
#

