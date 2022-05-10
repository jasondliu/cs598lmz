import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

import pdb
#pdb.set_trace()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

