import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

s2 = S()
s2.x = s.x
s2.y = s.y

print(s2.x, s2.y)

s2 = s

print(s2.x, s2.y)

s.x = 3

print(s2.x, s2.y)

s2.y = 4

print(s.x, s.y)

s2.x = 5

print(s.x, s.y)

s.y = 6

print(s2.x, s2.y)

s2 = S()
s2.x = s.x
s2.y = s.y

print(s2.x, s2.y)

s.x = 7

print(s2.x, s2.y)

s2.y
