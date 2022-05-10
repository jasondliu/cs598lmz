import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
# http://stackoverflow.com/questions/38459742/how-to-share-sqlite-database-between-process-in-python
# http://stackoverflow.com/questions/3093989/python-sqlite3-and-memory-sharing
# https://www.sqlite.org/sharedcache.html

# https://docs.python.org/2/library/ctypes.html
# http://stackoverflow.com/questions/23481549/python-ctypes-how-to-get-the-pointer-to-function-return-value-in-a-struct
# http://stackoverflow.com/questions/35773479/ctypes-function-with-struct-return-type-not-working-as-expected
# https://docs.python.org/2/library/ctypes.html#ctypes.create_string_buffer
# http://stackoverflow.com/questions/27055912/python-ctypes-how-to-get-the-
