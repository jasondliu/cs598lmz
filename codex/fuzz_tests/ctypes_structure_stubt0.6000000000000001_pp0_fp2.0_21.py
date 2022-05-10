import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(2)
    _fields_ = [('x', ctypes.c_int)]

print S.x
s = S()
print s.x
s.x = 1
print s.x
