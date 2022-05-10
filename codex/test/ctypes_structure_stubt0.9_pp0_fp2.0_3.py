import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2.0)
s = S()
print('hello', s.x)
