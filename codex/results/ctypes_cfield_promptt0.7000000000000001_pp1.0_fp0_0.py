import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ("d", ctypes.c_int),
        ("e", ctypes.c_int),
    ]

assert C.a.offset == ctypes.sizeof(ctypes.c_int)
assert C.b.offset == ctypes.sizeof(ctypes.c_int) * 2
assert C.c.offset == ctypes.sizeof(ctypes.c_int) * 3
assert C.d.offset == ctypes.sizeof(ctypes.c_int) * 4
assert C.e.offset == ctypes.sizeof(ctypes.c_int) * 5

assert C.b.offset == C.a.offset + C.a.size
assert C.c.offset == C.b.offset + C.b.size
assert C.d.offset == C.c.offset + C.c.size
assert C.
