import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2
print(s.x, s.y)

s.x = 3
s.y = 4
print(s.x, s.y)

s.x = 5
s.y = 6
print(s.x, s.y)

s.x = 7
s.y = 8
print(s.x, s.y)

s.x = 9
s.y = 10
print(s.x, s.y)

s.x = 11
s.y = 12
print(s.x, s.y)

s.x = 13
s.y = 14
print(s.x, s.y)

s.x = 15
s.y = 16
print(s.x, s.y)

s.x = 17
s.y = 18
print(s.x, s.y)

s.x = 19
s.y = 20
