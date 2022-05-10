import ctypes
# Test ctypes.CFUNCTYPE()
from ctypes import *
import _ctypes_test

try:
    ctypes.pythonapi
except AttributeError:
    raise Exception("This test requires Python 2.5 or later")

# This test is only runnable on Windows.  It tests the
# ctypes.WINFUNCTYPE() function.

if sys.platform != "win32":
    raise Exception("This test is only for Windows")

if sizeof(c_void_p) != sizeof(c_ulong):
    raise Exception("sizeof(c_void_p) != sizeof(c_ulong)")

# XXX This test is not very good, it only tests that the
# function pointer can be called.

# XXX This test is not finished.

# XXX This test is not run automatically.

# XXX This test is not runnable on 64-bit Windows.

# XXX This test is not runnable on Windows CE.

# XXX This test is not runnable on Windows XP 64-bit.

# XXX This test is not runnable on Windows Vista 64-bit.

