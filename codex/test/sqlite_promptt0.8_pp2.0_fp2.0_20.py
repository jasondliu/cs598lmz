import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect, without locking
# code is from the 3.2.2 sqlite3 python file, with the
# TRY_LOCK changed to NO_LOCK
