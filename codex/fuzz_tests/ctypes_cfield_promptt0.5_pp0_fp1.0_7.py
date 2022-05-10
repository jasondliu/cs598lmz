import ctypes
# Test ctypes.CField instance

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

assert X.a.__class__ is ctypes.CField
assert X.b.__class__ is ctypes.CField
assert X.a.name == "a"
assert X.b.name == "b"
assert X.a.offset == 0
assert X.b.offset == ctypes.sizeof(ctypes.c_int)
assert X.a.size == ctypes.sizeof(ctypes.c_int)
assert X.b.size == ctypes.sizeof(ctypes.c_int)
assert X.a.ctype == ctypes.c_int
assert X.b.ctype == ctypes.c_int

# Test ctypes.CField instance

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_
