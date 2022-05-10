import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [
        ('foo', ctypes.c_int, 1),
        ('bar', ctypes.c_int, 1),
        ('baz', ctypes.c_int, 1),
        ('qux', ctypes.c_int, 1),
        ('fred', ctypes.c_int, 1),
        ('s', ctypes.c_int, 1),
        ('g', ctypes.c_int, 1),
        ('h', ctypes.c_int, 1),
        ('i', ctypes.c_int, 1),
        ('j', ctypes.c_int, 1),
        ('k', ctypes.c_int, 1),
        ('l', ctypes.c_int, 1),
        ('m', ctypes.c_int, 1),
        ('n', ctypes.c_int, 1),
        ('o', ctypes.c_int, 1),
        ('p', ctypes.c_int, 1),
        ('q', ctypes.c_int, 1),
        ('r', ctypes
