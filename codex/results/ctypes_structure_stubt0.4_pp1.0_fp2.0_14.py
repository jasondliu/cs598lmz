import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S(1, 2)
print s.x
print s.y

s.x = 3
print s.x

s.y = 4
print s.y

print s[0]
print s[1]

s[0] = 5
print s.x

s[1] = 6
print s.y

s[0] = 7
print s[0]

s[1] = 8
print s[1]

print s.x
print s.y

print s[0]
print s[1]

print s[0]
print s[1]

print s.x
print s.y
