import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('file:test.db?mode=ro', uri=True)
# Test sqlite3.connect('file:test.db?mode=rw', uri=True)
# Test sqlite3.connect('file:test.db?mode=rwc', uri=True)
# Test sqlite3.connect('file:test.db?mode=memory', uri=True)
# Test sqlite3.connect('file:?mode=memory&cache=shared', uri=True)

# TODO(gps): test timeout, detect_types, isolation_level,
#            check_same_thread, factory, cached_statements,
#            and the rest of the connect() arguments.

# TODO(gps): test all the Connection and Cursor methods and attributes.

# TODO(gps): test executemany()

# TODO(gps): test the row_factory attribute.

# TODO(gps): test the text_factory attribute
