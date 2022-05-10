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

# https://github.com/python/cpython/blob/master/Modules/_sqlite/cache.h
# https://github.com/python/cpython/blob/master/
