import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# This is the only way to get the sqlite3 module to use the shared cache.
# It is not documented anywhere.
#
# The shared cache is a way to share the page cache between multiple
# connections.  This is useful for multi-threaded applications.
#
# The shared cache is enabled by default in the sqlite3 module.  However,
# the shared cache is only used if the database connection is opened using
# the URI filename "file:memory:?cache=shared".
#
# The shared cache is not used if the database connection is opened using
# the URI filename "file:memory:".
#
# The shared cache is not used if the database connection is opened using
# the filename ":memory:".
#
# The shared cache is not used if the database connection is opened using
# the filename "".
#
# The shared cache is not used if the database connection is opened using
# the filename None.
#
# The shared cache is not used if the database connection is opened using
# the filename "file:memory:?cache=private".
#
