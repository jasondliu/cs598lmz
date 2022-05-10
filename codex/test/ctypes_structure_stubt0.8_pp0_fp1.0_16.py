import ctypes

class S(ctypes.Structure):
    x = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    y = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

s = S()
s.x = None
s.y = s.x

s.x = s.y
s.y = None
s.x = None
