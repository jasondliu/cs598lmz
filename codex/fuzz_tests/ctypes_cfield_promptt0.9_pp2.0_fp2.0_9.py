import ctypes
# Test ctypes.CField
class Fields(ctypes.Structure):
    _fields_ = [("a", ctypes.c_ubyte),
                ("b", ctypes.c_ubyte, 4),
                ("c", ctypes.CField, 3),
                ("d", ctypes.c_ubyte, 7)]

f = Fields()
f.a = 5
print(f.a)
f.b = 2
print(f.b)
f.c = 3
print(f.c)
f.d = 6
print(f.d)

# Test new method found in ctypes-gcc49
try:
    print(ctypes.alignment(ctypes.c_double))
    print(ctypes.alignment(ctypes.c_longdouble))
    print(ctypes.alignment(ctypes.c_float))
except AttributeError: pass

# Test ctypes.Union
class TestUnion(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char),

