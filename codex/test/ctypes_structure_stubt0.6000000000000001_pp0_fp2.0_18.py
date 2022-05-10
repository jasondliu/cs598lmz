import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 4
s.y = 5

a = ctypes.cast(id(s), ctypes.POINTER(S))

