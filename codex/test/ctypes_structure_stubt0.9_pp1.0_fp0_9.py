import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
str(s)
s.x = 1
s.y = 1
str(s) # expected "&lt;ctypes.Structure object at 0x000000000000002...&gt;"
