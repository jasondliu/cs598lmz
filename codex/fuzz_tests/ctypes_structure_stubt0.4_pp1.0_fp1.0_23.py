import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x)
print(s.y)
print(s.z)

print(s)
print(s.x)
print(s.y)
print(s.z)

s.x = 5
s.y = 6
s.z = 7

print(s)
print(s.x)
print(s.y)
print(s.z)

print(s[0])
print(s[1])
print(s[2])

s[0] = 9
s[1] = 10
s[2] = 11

print(s)
print(s.x)
print(s.y)
print(s.z)
