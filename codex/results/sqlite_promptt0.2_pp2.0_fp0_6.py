import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# TODO:
# - Add a way to specify the number of threads to use
# - Add a way to specify the number of iterations to run
# - Add a way to specify the number of rows to insert
# - Add a way to specify the number of rows to select
# - Add a way to specify the number of rows to update
# - Add a way to specify the number of rows to delete
# - Add a way to specify the number of rows to insert, select, update, and delete
# - Add a way to specify the number of rows to insert, select, update, and delete per thread
# - Add a way to specify the number of rows to insert, select, update, and delete per thread per iteration
# - Add a way to specify the number of rows to insert, select, update, and delete per thread per iteration per connection
# - Add a way to specify the number of rows to insert, select, update, and delete per thread per iteration per connection per database
# - Add a way to specify the number of rows to insert, select, update, and delete per thread per iteration
