import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()

s.x = 5
s.y = 6

print(s.x, s.y)

p = ctypes.pointer(s)

print(p.contents.x, p.contents.y)

p.contents.x = 10
p.contents.y = 20

print(p.contents.x, p.contents.y)

print(s.x, s.y)

print(s.x, s.y)
