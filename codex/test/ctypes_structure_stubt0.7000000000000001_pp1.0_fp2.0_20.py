import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 5
s.y = 4

s_p = ctypes.pointer(s)
s_p.contents.x = 10
