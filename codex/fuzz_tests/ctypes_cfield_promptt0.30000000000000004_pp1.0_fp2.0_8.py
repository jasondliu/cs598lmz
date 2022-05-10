import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
assert X.a.offset == 0
assert X.b.offset == 4
assert X.a.size == 4
assert X.b.size == 4
assert X.a.index == 0
assert X.b.index == 1
assert X.a.bits == 32
assert X.b.bits == 32
assert X.a.pack == 1
assert X.b.pack == 1
assert X.a.alignment == 4
assert X.b.alignment == 4
assert X.a.type is ctypes.c_int
assert X.b.type is ctypes.c_int
assert X.a.name == "a"
assert X.b.name == "b"
assert X.a.ctype is ctypes.c_int
assert X.b.ctype is ctypes.c_int
assert X.a.shape == ()
assert X.b.shape == ()
assert X.a.strides ==
