import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

class U(ctypes.Union):
    _fields_ = [("x", ctypes.c_void_p),
                ("y", ctypes.c_void_p)]

for T in S, U:
    t = T()
    t.x = 1
