import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()

S.x.offset = lambda obj: ctypes.addressof(obj)
S.y.offset = lambda obj: ctypes.addressof(obj) + ctypes.sizeof(ctypes.c_float)

s = S()
s.x = 1.0
s.y = 2.0

