import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# This is a hack to get around the fact that we can't pass a ctypes
# object to a different thread.  We create a global variable that
# holds the ctypes object, and then we pass the address of the global
# variable to the other thread.  The other thread then uses the
# address to get the ctypes object.

# This is a hack to get around the fact that we can't pass a ctypes
# object to a different thread.  We create a global variable that
# holds the ctypes object, and then we pass the address of the global
# variable to the other thread.  The other thread then uses the
# address to get the ctypes object.

# This is a hack to get around the fact that we can't pass a ctypes
# object to a different thread.  We create a global variable that
# holds the ctypes object, and then we pass the address of the global
# variable to the other thread.  The other thread then uses the
# address to get the ctypes object.

# This is a hack to get
