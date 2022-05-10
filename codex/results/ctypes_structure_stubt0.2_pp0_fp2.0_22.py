import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

print(ctypes.sizeof(s))
print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))

print(ctypes.string_at(ctypes.addressof(s), ctypes.sizeof(s)))

print(ctypes.cast(ctypes.addressof(s), ctypes.POINTER(ctypes.c_int)))

p = ctypes.cast(ctypes.addressof(s), ctypes.POINTER(ctypes.c_int))
print(p[0], p[1])

p[0] = 3
p[1] = 4
print(s.x, s.y)

print(ctypes.string_at(ctypes.addressof(s), ctypes.sizeof(s)))


