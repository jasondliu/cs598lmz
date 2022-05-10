import ctypes
# Test ctypes.CField structure
#
# In addition to being a convenient way to represent a field
# specification in a C structure, CField is also a convenient way to
# represent a field specification in a python class.  Here is a
# test.

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ]

class Y(ctypes.Structure):
    _fields_ = [
        (X, "a", 1),
        (X, "b", 1),
        ]

    def __init__(self):
        pass

assert Y.a.offset == 0
assert Y.b.offset == ctypes.sizeof(X)

print("TEST OK")
