import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

# This is a pointer to a S structure
p = ctypes.pointer(s)

print(p.contents.x, p.contents.y, p.contents.z)

# This is a pointer to a pointer to a S structure
pp = ctypes.pointer(p)

print(pp.contents.contents.x, pp.contents.contents.y, pp.contents.contents.z)

# This is a pointer to a pointer to a pointer to a S structure
ppp = ctypes.pointer(pp)

print(ppp.contents.contents.contents.x, ppp.contents.contents.contents.y, ppp.contents.contents.contents.z)

# This is a pointer to a pointer to
