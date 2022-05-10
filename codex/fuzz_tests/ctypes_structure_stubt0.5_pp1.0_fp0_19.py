import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 1

s2 = S()
s2.x = 2

s.x = s2.x

assert s.x == s2.x
