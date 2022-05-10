import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('s', S * 10)
    ]

class D(ctypes.Structure):
    _fields_ = [
        ('c', C * 10)
    ]

d = D()

# Segmentation fault
d.c[9].s[9].x = 5
