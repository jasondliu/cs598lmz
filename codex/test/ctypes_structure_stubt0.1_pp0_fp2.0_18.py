import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

s2 = S()
s2.x = 4
s2.y = 5
s2.z = 6

print(s2.x, s2.y, s2.z)

print(s.x, s.y, s.z)

s.x = 7
s.y = 8
s.z = 9

print(s.x, s.y, s.z)
print(s2.x, s2.y, s2.z)

s2 = s

print(s.x, s.y, s.z)
print(s2.x, s2.y, s2.z)

s.x = 10
s.y = 11
s.z = 12

