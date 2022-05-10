import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.CField),
        ('c', ctypes.c_int),
        ('d', ctypes.CField),
        ('e', ctypes.c_int),
        ('f', ctypes.CField),
    ]

class D(C):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.CField),
        ('c', ctypes.c_int),
        ('d', ctypes.CField),
        ('e', ctypes.c_int),
        ('f', ctypes.CField),
    ]

class E(D):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.CField),
        ('c', ctypes.c_int),
        ('d', ctypes.CField),
        ('e', ctypes.c_int),
        ('f', ctypes.C
