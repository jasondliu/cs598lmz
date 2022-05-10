import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect for being able to work on a database in memory. Not necessary, since there is only one instance of this database
# and it is thread-safe.
db = sqlite3.connect(":memory:")
db.row_factory = sqlite3.Row
db.execute("create table if not exists request (request_id integer primary key, endpoint text, time integer, request_body text)")
# It is possible to have multiple threads writing at the same time to a database created like this. It's ok
db.execute("create table if not exists response (response_id integer primary key, request_id integer, time integer, response_body text)")
# This table will have at most one entry. It's more practical to have a table than a variable, so all threads can access it
db.execute("create table if not exists no_response (request_id integer primary key, time integer)")
db.commit()

# Since there is only one instance of this database, only one cursor to that database makes sense
cursor = db.cursor()

