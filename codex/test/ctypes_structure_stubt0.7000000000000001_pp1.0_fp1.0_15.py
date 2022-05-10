import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

p = ctypes.POINTER(S)
s = S()

s.x = 1.0
s.y = 2.0

print(ctypes.cast(ctypes.pointer(s), p), s.x, s.y)

#p = ctypes.cast(p, ctypes.POINTER(ctypes.c_double))
