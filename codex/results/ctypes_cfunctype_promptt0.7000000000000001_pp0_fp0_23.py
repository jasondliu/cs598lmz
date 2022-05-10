import ctypes
# Test ctypes.CFUNCTYPE

# Here's a C function
# int varargs_func(int format, ...) { ... }

# We need to tell ctypes how a variable number of arguments is passed
# in C. This information varies from platform to platform, so
# ctypes uses a callback function to determine the correct argument
# passing mechanism.

if sys.platform == "win32":
    WINFUNCTYPE = ctypes.WINFUNCTYPE
else:
    WINFUNCTYPE = None

from ctypes import *
from ctypes.wintypes import *

class COORD(Structure):
    _fields_ = [
        ("X", c_short),
        ("Y", c_short)
    ]

class SMALL_RECT(Structure):
    _fields_ = [
        ("Left", c_short),
        ("Top", c_short),
        ("Right", c_short),
        ("Bottom", c_short)
    ]

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    _fields_ = [
        ("dwSize
