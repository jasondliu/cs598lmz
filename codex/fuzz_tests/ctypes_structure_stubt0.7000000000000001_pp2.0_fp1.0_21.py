import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32(3)

S._fields_ = [('x', ctypes.c_int32)]

s = S()
print s.x
s.x = 4
print s.x
