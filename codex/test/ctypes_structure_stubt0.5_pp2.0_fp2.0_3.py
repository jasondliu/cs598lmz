import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

s = S()
s.x = 1
s.y = 2

# test __getattr__
