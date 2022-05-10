import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble(123.0)
    y = ctypes.c_longdouble(234.0)

s = S()
p = ctypes.pointer(s)

