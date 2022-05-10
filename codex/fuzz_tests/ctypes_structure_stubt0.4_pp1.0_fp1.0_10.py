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

print(ctypes.sizeof(s))

print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))
print(ctypes.addressof(s.z))

p = ctypes.pointer(s)
print(ctypes.addressof(p.contents))
print(ctypes.addressof(p.contents.x))
print(ctypes.addressof(p.contents.y))
print(ctypes.addressof(p.contents.z))

print(p.contents.x, p.contents.y, p.contents.z)

p.contents.x = 10
p.contents.y = 20

