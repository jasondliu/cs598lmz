import ctypes
# Test ctypes.CField instance

class C(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_long),
        ("b", ctypes.c_long),
        ("c", ctypes.c_long),
    ]

c = C()
print(c.a)
print(c.b)
print(c.c)
print(C.a)
print(C.b)
print(C.c)
