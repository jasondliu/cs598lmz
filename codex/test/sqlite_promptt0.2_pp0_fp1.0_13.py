import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# The following code is taken from the sqlite3 module documentation.
# It is used to create a shared memory connection to the database.

def adapt_date(val):
    return val.isoformat()

def convert_date(val):
    return datetime.datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")

sqlite3.register_adapter(datetime.date, adapt_date)
sqlite3.register_converter("date", convert_date)

# End of code taken from sqlite3 module documentation.

# The following code is taken from the sqlite3 module documentation.
# It is used to create a shared memory connection to the database.

def adapt_date(val):
    return val.isoformat()

def convert_date(val):
    return datetime.datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")

