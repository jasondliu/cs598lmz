import ctypes
# Test ctypes.CField

# CField objects are used in Structure and Union definitions. They are
# containers for field information like offset, type, etc.
# This test checks the creation of a CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

assert X.a.offset == 0
assert X.a.size == ctypes.sizeof(ctypes.c_int)
assert X.a.name == "a"
assert X.a.index == 0
assert X.a.type is ctypes.c_int

try:
    X.a.offset = 1
except ValueError:
    pass
else:
    raise Exception

try:
    X.a.size = 1
except ValueError:
    pass
else:
    raise Exception

try:
    X.a.name = "b"
except ValueError:
    pass
else:
    raise Exception

try:
    X.a.type = ctypes.c_short
except ValueError:
    pass
else:
    raise Exception

assert X
