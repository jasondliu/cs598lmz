import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S(1, 2, 3)
print(s.x)
print(s.y)
print(s.z)

print(s[0])
print(s[1])
print(s[2])

print(s[-1])
print(s[-2])
print(s[-3])

print(s[0:2])
print(s[0:3])
print(s[1:3])

print(s[:])
print(s[::2])
print(s[::-1])

print(s[0:0])
print(s[1:1])
print(s[2:2])

print(s[0:0:1])
print(s[1:1:1])
print(s[2:2:1])

print(s[0:0:2])
print(s[1:1:2])
print(s[2:2:2])
