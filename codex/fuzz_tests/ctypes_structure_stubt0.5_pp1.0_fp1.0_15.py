import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8()
    y = ctypes.c_uint8()
    z = ctypes.c_uint8()

s = S()
s.x = 3
s.y = 2
s.z = 1

print(s.x)
print(s.y)
print(s.z)

print(s.x.value)
print(s.y.value)
print(s.z.value)

print(ctypes.sizeof(s))
print(ctypes.sizeof(s.x))
print(ctypes.sizeof(s.y))
print(ctypes.sizeof(s.z))

print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))
print(ctypes.addressof(s.z))

print(ctypes.addressof(s.x) - ctypes.addressof(s))
print(ctypes.addressof(s.y) - ctypes.
