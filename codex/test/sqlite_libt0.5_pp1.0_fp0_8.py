import ctypes
import ctypes.util
import threading
import sqlite3
import time

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Set the name of the output file here. This file will have one line
# for each write() call. Each line will have the following fields,
# separated by single spaces:
# 1. The string "write"
# 2. The return value from the write() call
# 3. The file descriptor that was written to
# 4. The number of bytes written
# 5. The text that was written, in quotes.
# Note that this file will be overwritten if it already exists.
trace_output_filename = "fs_trace.txt"

# Set the name of the database file here. This file will have one
# table named writes, with the following schema:
#
#    CREATE TABLE writes(id INTEGER PRIMARY KEY, fd INTEGER, size INTEGER, data TEXT);
#
# There will be one row for each write() call.
sqlite_output_filename = "fs_trace.db"

# fd -> (lock, offset, data)

