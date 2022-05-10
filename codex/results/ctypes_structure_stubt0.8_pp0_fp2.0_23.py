import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    _fields_ = [("x", ctypes.c_short),
                ("pad", ctypes.c_char*6)]

s = S()
print s.x, ctypes.addressof(s.x)

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_short),
                ("pad", ctypes.c_char*6)]

s = S2()
print s.x, ctypes.addressof(s.x)
