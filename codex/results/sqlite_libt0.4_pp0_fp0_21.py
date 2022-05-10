import ctypes
import ctypes.util
import threading
import sqlite3
import os

# This is the name of the database file.
DB_FILE = "kvstore.db"

# This is the name of the table we will use to store the key/value pairs.
TABLE_NAME = "kvstore"

# This is the name of the column we will use to store the keys.
KEY_COLUMN_NAME = "key"

# This is the name of the column we will use to store the values.
VALUE_COLUMN_NAME = "value"

# This is the name of the column we will use to store the timestamps.
TIMESTAMP_COLUMN_NAME = "timestamp"

# This is the maximum number of key/value pairs we will store in the database.
MAX_NUM_PAIRS = 100

# This is the maximum length of a key or value.
MAX_LENGTH = 1024

# This is the maximum number of threads we will create.
MAX_NUM_THREADS = 100

# This is the maximum number of times we will try to acquire the lock.
MAX_LOCK_ATTEMPTS
