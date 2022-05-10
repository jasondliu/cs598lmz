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

print(s.x)
print(s.y)

print(s2.x)
print(s2.y)

s.x = 5
s.y = 6

s2.x = 7
s2.y = 8

print(s.x)
print(s.y)

print(s2.x)
print(s2.y)
