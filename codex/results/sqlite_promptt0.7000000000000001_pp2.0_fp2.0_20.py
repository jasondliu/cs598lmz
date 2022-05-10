import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import sqlite3
# Test sqlite3.connect()
try:
    # If we have a standalone SQLite3, then use it
    from pysqlite2 import dbapi2 as sqlite3
except ImportError:
    # Otherwise, use the Python-supplied SQLite3
    import sqlite3

from i2p import datatypes
from i2p import util
from i2p import tunnels
from i2p import crypto
from i2p import b32

SAM_API_VERSION = 3

def require_libsam(message):
    """
    Raise an error if the SAM library cannot be found.
    """
    if not ctypes.cdll.LoadLibrary(ctypes.util.find_library("sam")):
        raise ImportError(message)

# XXX: This is not exactly correct.  We should probably be using ctypes.POINTER
#      to represent pointers to other types.
sam_field_types = {
    "string": ctypes.c_char_p,
    "string_list": ctypes.c_char_p,

