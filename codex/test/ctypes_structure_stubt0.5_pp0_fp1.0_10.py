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

print(s.x + s.y + s.z)

s.x = s.y = s.z = 10

print(s.x)
print(s.y)
print(s.z)

print(s.x + s.y + s.z)

print(s)

print(s.x)
print(s.y)
print(s.z)

print(s.x + s.y + s.z)

s.x = s.y = s.z = 100

print(s.x)
print(s.y)
print(s.z)

print(s.x + s.y + s.z)

print(s)
