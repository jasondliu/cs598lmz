import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()

s = S()
s.x

s.x = 23.45
s.x

S.x
S.x.__doc__
