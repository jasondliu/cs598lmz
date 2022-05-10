import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char_p)]

class D(ctypes.Structure):
    _fields_ = [("d", ctypes.c_int),
                ("c", C)]

class E(ctypes.Structure):
    _fields_ = [("e", ctypes.c_int),
                ("d", D)]

class F(ctypes.Structure):
    _fields_ = [("f", ctypes.c_int),
                ("e", E)]

f = F(1, E(2, D(3, C(4, b"abc"))))
print(f.f)
print(f.e.e)
print(f.e.d.d)
print(f.e.d.c.a)
print(f.e.d.c.b)

# Test ctypes.CArray

a = (ctypes.c_int * 4)(1, 2, 3, 4)

