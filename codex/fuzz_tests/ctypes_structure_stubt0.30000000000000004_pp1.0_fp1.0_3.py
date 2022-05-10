import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

# ctypes.string_at(s, ctypes.sizeof(s))

# ctypes.memmove(s, ctypes.string_at(s, ctypes.sizeof(s)), ctypes.sizeof(s))

# print s.x, s.y
