import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

# This is a bug:
s = S()
print s.x
s.x = 1
print s.x

# This is not a bug:
s = S()
print s.x
s.x = 1
print s.x
