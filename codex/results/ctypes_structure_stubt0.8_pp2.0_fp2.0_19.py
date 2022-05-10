import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    p = ctypes.POINTER(x)

s = S()

s.x = 42
s.p = ctypes.pointer(s.x)

print s.x, s.p.contents

s.x = 24
print s.x, s.p.contents
