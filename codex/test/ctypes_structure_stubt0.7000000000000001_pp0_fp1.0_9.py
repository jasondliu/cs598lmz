import ctypes

class S(ctypes.Structure):
    x = None

    _fields_ = [('x', ctypes.c_int)]

s = S()
print(s.x)
