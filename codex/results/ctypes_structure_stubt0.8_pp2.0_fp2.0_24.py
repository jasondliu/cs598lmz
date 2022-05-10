import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
print s.x
print s.x
x = ctypes.byref(s) + 1
print s.x, s.y
