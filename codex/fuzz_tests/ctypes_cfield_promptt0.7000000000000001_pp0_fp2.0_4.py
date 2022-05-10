import ctypes
# Test ctypes.CField
class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                (ctypes.CField("c", ctypes.c_int), ctypes.c_ulong)]

f = F()
f.a = 2
f.b = 3
assert f.c == 5

# Test ctypes.c_enum
class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                (ctypes.c_enum("c", ctypes.c_ulong), ctypes.c_ulong)]

f = F()
f.a = 2
f.b = 3
assert f.c == 5

# Test ctypes.c_enum with "type"
class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                (ctypes.c_enum("c
