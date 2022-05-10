import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

s2 = S()
s2.x = 3
s2.y = 4

print(s.x, s.y)
print(s2.x, s2.y)

s2 = s
s2.x = 5
s2.y = 6

print(s.x, s.y)
print(s2.x, s2.y)

s2 = S()
s2.x = 3
s2.y = 4

print(s.x, s.y)
print(s2.x, s2.y)
