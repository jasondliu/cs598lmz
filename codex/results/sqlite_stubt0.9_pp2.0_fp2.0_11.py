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

    return 100

prepare_threading_local_callback(my_cb)

#
# Construct binary - from sqlite3.c
#

libsqlite3_source = r"""
//
// (c) 2012, 2013, 2014 Nathaniel J. Smith <njs@pobox.com>
//
// This work is made available to you under the terms of the Creative
// Commons CC-BY-NC license version 4.0 or any later version. A copy of
// the license is included in the file LICENSE.TXT distributed as part
// of this software.
//
// This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
// INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE.
//
//
// Build with
//
//    gcc -ldl -shared -o libsqlite3.so -O3 -fPIC \
//        -I/usr/include/python3.3m -I/usr/include/x86_64-linux-gnu/python3.3m \
//       
