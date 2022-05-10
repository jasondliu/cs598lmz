import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect().
_db = sqlite3.connect(':memory:')
#
#----------------------------------------------------------------------------
#
# The ctypes package comes with Python 2 (since version 2.5).  On Linux
# distributions, the libm.so library is either in /usr/lib or /lib.  On
# Windows and Mac OS systems, consider installing MinGW and the GNU MP
# library.
_dll = ctypes.cdll.LoadLibrary(ctypes.util.find_library('m'))

# Function prototypes (see man 3 cos, man 3 sin and etc.).
_cos = _dll.cos
_cos.argtypes = (ctypes.c_double,)
_cos.restype = ctypes.c_double
_sin = _dll.sin
_sin.argtypes = (ctypes.c_double,)
_sin.restype = ctypes.c_double
_atan2 = _dll.atan2
_atan2.argtypes = (ctypes.c_double, ctypes.c_double,)
_atan2.restype = ctypes.c_double
