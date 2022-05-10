import ctypes
# Test ctypes.CFUNCTYPE.errcheck
from ctypes import *
from ctypes.test import need_symbol

test_target = "win32"

# the c int is smaller than a python int, and we must be careful
# to do the cast at the right time.

def test_cast(result, func, args):
    if result == -1:
        raise IOError(ctypes.get_errno())
    return result

# This function doesn't need a prototype
GetStdHandle = windll.kernel32.GetStdHandle
GetStdHandle.restype = c_uint32

GetStdHandle.errcheck = test_cast

# returns 0 when we pass NULL as handle
handle = GetStdHandle(0)

assert not handle

# Here we need a prototype (because the function is not exported
# without stdcall convention)
PROTOTYPE = WINFUNCTYPE(c_uint32, c_uint32)
GetStdHandle = PROTOTYPE(("GetStdHandle", windll.kernel32))

# does this also work for win functions?
