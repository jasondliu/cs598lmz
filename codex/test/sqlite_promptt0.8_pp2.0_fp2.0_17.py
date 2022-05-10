import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

try:
    import _sqlite3
except ImportError:
    print("SKIP")
    raise SystemExit

# Test case for: (1) https://github.com/pfalcon/micropython-lib/issues/455
# and (2) https://github.com/pfalcon/micropython-lib/issues/456

# The following structure reproduces the structure of a Python object that
# may be passed to sqlite3_bind_pointer().

class X(ctypes.Structure): pass

class T(threading.Thread):

    def run(self):
        try:
            sqlite3.connect(":memory:")
        except sqlite3.OperationalError:
            print("SQLITE_OK")


t = T()
t.start()
t.join()

# The following case reproduces the issue from
# https://forum.micropython.org/viewtopic.php?f=16&t=6791

