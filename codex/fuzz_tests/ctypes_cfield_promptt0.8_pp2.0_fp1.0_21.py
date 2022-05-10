import ctypes
# Test ctypes.CField and ctypes.Field

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_float),
                ("b", ctypes.c_float)]
    c = ctypes.c_float

class Y(ctypes.Structure):
    _fields_ = [("x", X), ("d", ctypes.c_float)]

y = Y()
total = 0
for f in y._fields_:
    total += f[1].size
assert y.x.a == 0.0
assert y.x.b == 0.0
assert y.d == 0.0

assert total == ctypes.sizeof(y) == 16

class Z(ctypes.Structure):
    _fields_ = [("x", X),
                ("d", ctypes.c_float),
                ("x", X)]

import sys
if sys.platform == "cli":
    import System
    raise System.NotImplementedException()
else:
    try:
        Z()
    except ValueError:
        pass
    else:
