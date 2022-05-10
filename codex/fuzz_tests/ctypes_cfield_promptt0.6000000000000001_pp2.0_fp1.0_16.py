import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_char),
        ('c', ctypes.c_double),
        ('d', ctypes.c_char),
        ('e', ctypes.c_char),
        ('f', ctypes.c_int),
        ('g', ctypes.c_int),
        ('h', ctypes.c_char),
        ]
    _anonymous_ = 'd', 'e', 'h'

x = X()
print x.a
print x.b
print x.c
print x.f

# Test ctypes.CField.from_address
class X(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_char),
        ('c', ctypes.c_double),
        ('d', ctypes.c_char),
        ('e', ctypes.c_char),
        ('f', ctypes.
