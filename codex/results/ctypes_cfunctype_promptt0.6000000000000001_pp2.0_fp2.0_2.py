import ctypes
# Test ctypes.CFUNCTYPE
try:
    if ctypes.CFUNCTYPE is None:
        raise ImportError()
except AttributeError:
    raise ImportError()

from ctypes import CFUNCTYPE, POINTER, c_int32, c_int64, c_void_p

# See http://bugs.python.org/issue2983.  SF bug #973167.

# This segfaults
ctypes.CFUNCTYPE(c_int32, c_void_p)(lambda x: x)

# This works
ctypes.CFUNCTYPE(c_int32, c_void_p)(lambda x: c_int64(x).value)

# This works
ctypes.CFUNCTYPE(c_int64, c_void_p)(lambda x: x)

# This works
ctypes.CFUNCTYPE(c_int64, c_void_p)(lambda x: c_int64(x).value)

# This works
ctypes.CFUNCTYPE(c_void_p, c_void_
