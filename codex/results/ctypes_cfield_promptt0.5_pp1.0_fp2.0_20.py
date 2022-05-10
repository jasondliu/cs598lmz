import ctypes
# Test ctypes.CField 

class X(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
    ]

class Y(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', X),
        ('c', ctypes.c_int),
    ]

class Z(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', Y),
        ('c', ctypes.c_int),
    ]

z = Z()
print z.a
print z.b.a
print z.b.b.a
print z.b.b.b
print z.b.b.c
print z.b.c
print z.c

z.a = 1
z.b.a = 2
z.b.b.a = 3
z.b.b.b = 4
z
