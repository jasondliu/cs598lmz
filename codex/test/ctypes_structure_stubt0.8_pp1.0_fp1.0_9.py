import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2.5)
    y = ctypes.c_double()

s = S()
print(s.y)
