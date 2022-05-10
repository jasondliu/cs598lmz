import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# https://github.com/python/cpython/blob/master/Modules/_sqlite/cursor.c
# https://github.com/python/cpython/blob/master/Modules/_sqlite/connection.c
# https://github.com/python/cpython/blob/master/Modules/_sqlite/microprotocols.c
# https://github.com/python/cpython/blob/master/Modules/_sqlite/module.c
# https://github.com/python/cpython/blob/master/Modules/_sqlite/row.c
# https://github.com/python/cpython/blob/master/Modules/_sqlite/statement.c
# https://github.com/python/cpython/blob/master/Modules/_sqlite/util.c

# https://www.sqlite.org/c3ref/c_static.html
# https://www.sqlite.org/c3ref/c_config_covering_index_scan
