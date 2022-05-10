import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# Python 3.2 cannot use ctypes.WINFUNCTYPE on a 64-bit platform
# because the argument types are not defined.
if ctypes.sizeof(ctypes.c_void_p) == 8:
    winfunctype = ctypes.CFUNCTYPE
else:
    winfunctype = ctypes.WINFUNCTYPE

# The error message is:
#   TypeError: item 1 in _argtypes_ passes a union by value, which is
#   unsupported.

# The problem is that the argument types are not defined.

WNDPROC = winfunctype(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
WNDPROC(lambda h, m, w, l: 0)


# The error message is:
#   TypeError: item 1 in _argtypes_ passes a union by value, which is
#   unsupported.

# The problem is that the first argument type is not defined.

WNDPROC = winfunct
