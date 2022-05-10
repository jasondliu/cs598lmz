import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

a = S()
a.x = 3
a.y = 4

b = S()
b.x = 7
b.y = 8

S.x.__doc__ = "3"
S.y.__doc__ = "4"

