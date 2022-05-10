import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()
s.a = 2
s.b = 3
s.c = 4
s.d = 5
