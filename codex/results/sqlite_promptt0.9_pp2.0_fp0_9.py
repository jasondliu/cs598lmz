import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection()
sqlite3.threadsafety

# find libc shared library 0xe4e8e4b4e4a4
libc = ctypes.CDLL(
    ctypes.util.find_library('c'),
)

# 0xe4e8e4a4e4b4e4a4e8e4b4e5e1e5b5e5bd8f2e5bd90
# ts type: sqlite3_int64 
# FIXME: it might be better to use C type
ts = ctypes.c_longlong.from_buffer(libc.time(None))
# e4e8e4e1ece4b4e5e1e5b5e5bd8f2e5bd90
# iterate over table to fetch all modified files.
# XXX: better check modification time with 0xe4e8e4e1ece523e5e11ee5e863e7e861e5e1 ,
#      need to get timestamp
# XXX: cannot handle file deletion.
#      original file list needs to be
