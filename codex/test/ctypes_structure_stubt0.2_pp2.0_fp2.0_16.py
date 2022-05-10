import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.x + s.y)

print(s.x + s.y == 3)

print(s.x + s.y == 4)

print(s.x + s.y == 5)

print(s.x + s.y == 6)

print(s.x + s.y == 7)

print(s.x + s.y == 8)

print(s.x + s.y == 9)

print(s.x + s.y == 10)

print(s.x + s.y == 11)

print(s.x + s.y == 12)

print(s.x + s.y == 13)

print(s.x + s.y == 14)

print(s.x + s.y == 15)

