import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16()
    y = ctypes.c_int32()
    z = ctypes.c_int64()

s = S()
print(s.x)
print(s.y)
print(s.z)

print(type(s.x))
print(type(s.y))
print(type(s.z))

print(type(s.x) == ctypes.c_int16)
print(type(s.y) == ctypes.c_int32)
print(type(s.z) == ctypes.c_int64)

s.x = -1
s.y = -2
s.z = -3

print(s.x)
print(s.y)
print(s.z)

print(s.x == -1)
print(s.y == -2)
print(s.z == -3)
