import ctypes

class S(ctypes.Structure):
    x = 0
    _fields_ = [('x', ctypes.c_int)]

s = S()
print s.x
s.x = 1
print s.x
