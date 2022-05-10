import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2
print s.x, s.y

s2 = S()
s2.x = 3
s2.y = 4
print s2.x, s2.y

s2 = s
print s2.x, s2.y

s.x = 5
print s2.x, s2.y

s2.x = 6
print s.x, s.y

s2.x = 7
print s.x, s.y

s.x = 8
print s2.x, s2.y

s2 = S()
print s.x, s.y

s2.x = 9
print s.x, s.y

s.x = 10
print s2.x, s2.y

s2 = s
print s2.x, s2.y

s.x = 11
print s2.x, s2.y

s2.x =
