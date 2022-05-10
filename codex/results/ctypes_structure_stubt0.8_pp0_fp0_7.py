import ctypes

class S(ctypes.Structure):
    x = 123
    _fields_ = [('x', ctypes.c_int)]

S._pack_ = 4
S._fields_ = [('x', ctypes.c_int)]

print ctypes.sizeof(S)
