import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        (None, None),
        ("y", ctypes.c_int)
    ]

class Y(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.CField),
        ("b", ctypes.CField(None, None)),
        ("c", ctypes.CField("y"))
    ]


if sys.byteorder == "big":
    assert ctypes.sizeof(Y) == 24
else:
    assert ctypes.sizeof(Y) == 8

y = Y()
x = X()
x.x = 0x12345678
x.y = 0x87654321
y.a = x.x
y.b = x.x
y.c = x.y

assert y.a == 0x12345678
assert y.b == 0x12345678
assert y.c == 0x87654321
