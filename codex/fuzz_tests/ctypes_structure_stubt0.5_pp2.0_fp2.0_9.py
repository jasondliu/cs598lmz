import ctypes

class S(ctypes.Structure):
    x = 1
    y = 2
    _fields_ = [
        ('p', ctypes.POINTER(S)),
        ('s', S),
        ('i', ctypes.c_int),
        ('f', ctypes.c_float),
        ('d', ctypes.c_double),
        ('c', ctypes.c_char),
        ('b', ctypes.c_byte),
        ('a', ctypes.c_char * 5),
        ('z', ctypes.c_wchar),
        ('w', ctypes.c_wchar * 5),
        ('u', ctypes.c_ushort),
        ('l', ctypes.c_ulong),
        ('v', ctypes.c_void_p),
        ('t', ctypes.c_char_p),
        ('m', ctypes.c_char_p),
        ('r', ctypes.c_int * 2),
        ('q', ctypes.c_char * 2),
        ]

s = S()
s.p = ctypes.pointer(s)

import
