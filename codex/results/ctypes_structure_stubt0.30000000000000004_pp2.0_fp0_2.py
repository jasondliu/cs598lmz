import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
print(s.x, s.y)
s.x = 3
print(s.x, s.y)

s = S(4, 5)
print(s.x, s.y)
s.x = 6
print(s.x, s.y)

s = S(x=7)
print(s.x, s.y)
s.x = 8
print(s.x, s.y)

s = S(y=9)
print(s.x, s.y)
s.x = 10
print(s.x, s.y)

s = S(x=11, y=12)
print(s.x, s.y)
s.x = 13
print(s.x, s.y)

s = S(y=14, x=15)
print(s.x, s.y)
s.x = 16
print(s.x, s.y)

