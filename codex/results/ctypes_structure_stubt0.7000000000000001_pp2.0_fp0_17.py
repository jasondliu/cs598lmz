import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]

s = S()
print s.x, s.y
s.x = 1.0
print s.x, s.y
