import ctypes
# Test ctypes.CField.

class X(ctypes.Structure):
    pass

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

assert ctypes.sizeof(Y) == ctypes.sizeof(X)
assert ctypes.sizeof(Y()) == ctypes.sizeof(X)

class Z(ctypes.Structure):
    y = ctypes.CField(X)

assert ctypes.sizeof(Z) == ctypes.sizeof(X)
assert ctypes.sizeof(Z()) == ctypes.sizeof(X)
