import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_float),
        ('z', ctypes.c_double),
        ('w', ctypes.c_char * 10),
        ('u', ctypes.c_char * 10),
        ('v', ctypes.c_char * 10),
        ('s', ctypes.c_char * 10),
        ('t', ctypes.c_char * 10),
        ('a', ctypes.c_char * 10),
        ('b', ctypes.c_char * 10),
        ('c', ctypes.c_char * 10),
        ('d', ctypes.c_char * 10),
        ('e', ctypes.c_char * 10),
        ('f', ctypes.c_char * 10),
        ('g', ctypes.c_char * 10),
        ('h', ctypes.c_char * 10),
        ('i', ctypes.c_char * 10),
        ('j', ctypes
