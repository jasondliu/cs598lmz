import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_char),
                ('c', ctypes.c_char),
                ('d', ctypes.c_char),
                ('e', ctypes.c_char),
                ('f', ctypes.c_char),
                ('g', ctypes.c_char),
                ('h', ctypes.c_char),
                ('i', ctypes.c_char),
                ('j', ctypes.c_char),
                ('k', ctypes.c_char),
                ('l', ctypes.c_char),
               ]

class Y(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_char),
                ('c', ctypes.c_char),
                ('d', ctypes.c_char),
                ('e', ctypes.c_char),
                ('f', ctypes.c_char),
                ('g', c
