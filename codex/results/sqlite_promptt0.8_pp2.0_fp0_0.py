import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.set_load_extension
import sys
if sys.platform=='win32':
    from thread import start_new_thread as start_new_thread
else:
    from _thread import start_new_thread as start_new_thread

libtest = ctypes.CDLL(ctypes.util.find_library('test'))

# Allocate a buffer we can use to pass strings around
size = 1024
buf = ctypes.create_string_buffer(size)

def create_function(conn, name, func, args=None, deterministic=False):
    if args is None:
        args = ""
    conn.create_function(name, len(args), func, deterministic=deterministic)

con = sqlite3.connect(":memory:")

# FIXME: should we use a subclass of Exception?
class BlobTooBigError(Exception):
    pass

def blob_from_buffer(buf, length):
    if length>size:
        raise BlobTooBigError
    return buf

class ThreadedTests(unittest.TestCase
