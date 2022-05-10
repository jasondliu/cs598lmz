import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
    ]
    _anonymous_ = [
        ('d', ctypes.c_int),
        ('e', ctypes.c_int),
    ]

class D(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', C),
    ]

class E(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', C),
    ]
    _anonymous_ = [
        ('d', ctypes.c_int),
        ('e', ctypes.c_int),
    ]

def check(name, field):
    print(name, field.offset, field.size)


