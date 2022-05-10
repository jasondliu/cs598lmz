import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short(1)
    y = ctypes.c_long(2)

s = S()
p = ctypes.pointer(s)
pi = ctypes.cast(p, ctypes.POINTER(ctypes.c_long))
print(s.x)
print(s.y)
print(p.contents.x)
print(p.contents.y)
print(p[0])
print(p[1])
print(pi[0])
print(pi[1])
