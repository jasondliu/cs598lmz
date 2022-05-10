import ctypes
# Test ctypes.CField.

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    class Y(ctypes.Structure):
        _fields_ = [("b", ctypes.c_int)]

assert X.a.__class__ is ctypes.CField
assert X.Y.b.__class__ is ctypes.CField

# Test ctypes.CField.from_address.

a = ctypes.c_int(0)
b = ctypes.c_int(0)
c = ctypes.c_int(0)

d = ctypes.CField.from_address(id(a), ctypes.c_int)
assert d == a
assert d.value == 0
d.value = 42
assert a.value == 42
assert d.value == 42

e = ctypes.CField.from_address(id(b), ctypes.c_int, 1)
assert e == b
assert e.value == 0
e.value = 42
assert b.value == 42
assert e.value ==
