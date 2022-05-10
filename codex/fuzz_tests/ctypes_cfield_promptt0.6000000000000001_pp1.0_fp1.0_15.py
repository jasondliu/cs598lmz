import ctypes
# Test ctypes.CField structure.

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int)
    ]

assert X.a.offset == 0
assert X.b.offset == ctypes.sizeof(ctypes.c_int)
assert X.c.offset == X.b.offset + ctypes.sizeof(ctypes.c_int)
