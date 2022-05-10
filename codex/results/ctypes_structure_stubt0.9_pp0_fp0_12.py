import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(5)
    _fields_ = [('x', ctypes.c_char),
                ('x', ctypes.c_unichar)]

print (S.x)
