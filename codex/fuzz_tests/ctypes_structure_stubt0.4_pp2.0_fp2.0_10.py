import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print s.x
print s.y

s.x = 42
s.y = 43
print s.x
print s.y

print ctypes.sizeof(s)

s2 = S()
s2.x = s.x
s2.y = s.y
print s2.x
print s2.y

s2.x = 44
s2.y = 45
print s.x
print s.y
