import ctypes
# Test ctypes.CField.from_address

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X), ("c", ctypes.c_int)]

y = Y()
y.x.a = 42
y.x.b = 12
y.c = 15

import sys
if sys.byteorder == "little":
    assert ctypes.c_int.from_address(ctypes.addressof(y.x)).value == 42
    assert ctypes.c_int.from_address(ctypes.addressof(y.x) + ctypes.sizeof(ctypes.c_int)).value == 12
    assert ctypes.c_int.from_address(ctypes.addressof(y.c)).value == 15
else:
    assert ctypes.c_int.from_address(ctypes.addressof(y.x)).value == 12
    assert ctypes.c_int.
