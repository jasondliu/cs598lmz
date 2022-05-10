import ctypes
# Test ctypes.CField and ctypes.Field.

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("_b", ctypes.c_int),
                ("", ctypes.c_int),
                ("c", ctypes.c_int),
                ("", ctypes.c_int),
                ctypes.CField("d", ctypes.c_int),
                ctypes.CField("", ctypes.c_int),
                ctypes.CField("e", ctypes.c_int),
                ctypes.CField("f", ctypes.c_int),
                ctypes.Field("g", ctypes.c_int, 4),
                ctypes.Field("h", ctypes.c_int, 1)]

print X.a.offset, X.a.size
print X._b.offset, X._b.size
print X.c.offset, X.c.size
print X.d.offset, X.d.size
print X.e.offset, X.e.size
print X.f.
