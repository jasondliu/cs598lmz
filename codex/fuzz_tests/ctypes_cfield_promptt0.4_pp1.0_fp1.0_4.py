import ctypes
# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [
        ('i', ctypes.c_int),
        ('j', ctypes.c_int),
        ('k', ctypes.c_int),
        ('l', ctypes.c_int),
        ('m', ctypes.c_int),
        ('n', ctypes.c_int),
    ]

print X.i
print X.j
print X.k
print X.l
print X.m
print X.n

# Test ctypes.CField.from_address

class Y(ctypes.Structure):
    _fields_ = [
        ('i', ctypes.c_int),
        ('j', ctypes.c_int),
        ('k', ctypes.c_int),
        ('l', ctypes.c_int),
        ('m', ctypes.c_int),
        ('n', ctypes.c_int),
    ]

y = Y()
y.i = 1
y.j = 2
y.
