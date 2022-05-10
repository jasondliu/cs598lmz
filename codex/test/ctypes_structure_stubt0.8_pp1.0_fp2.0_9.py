import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)
    y = ctypes.c_double(1.0)
    _pack_ = 1 #must be set to 1

s = S()
print(s)
s.y = 2.0
print(s)
