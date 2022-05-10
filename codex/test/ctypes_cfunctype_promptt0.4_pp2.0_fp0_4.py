import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

try:
    ctypes.CFUNCTYPE(ctypes.c_int)
except TypeError:
    raise Exception("CFUNCTYPE(ctypes.c_int) should not raise TypeError")

try:
    ctypes.CFUNCTYPE()
except TypeError:
    pass
else:
    raise Exception("CFUNCTYPE() should raise TypeError")

try:
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
except TypeError:
    pass
