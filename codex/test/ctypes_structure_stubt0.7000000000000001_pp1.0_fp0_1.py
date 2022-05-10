import ctypes

class S(ctypes.Structure):
    x = [ctypes.c_int, ctypes.c_int]

s = S()
s.x[0] = 1
s.x[1] = 2
