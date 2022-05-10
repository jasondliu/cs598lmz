import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    z = ctypes.c_int()

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x)
print(s.y)
print(s.z)

print(s)
print(s._fields_)

print(ctypes.sizeof(s))
print(ctypes.sizeof(S))

print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))
print(ctypes.addressof(s.z))

print(ctypes.string_at(ctypes.addressof(s), ctypes.sizeof(s)))
print(ctypes.string_at(ctypes.addressof(s.x), ctypes.sizeof(s.x)))
print(ctypes.string_at(ctypes.addressof(s.y), ctypes.sizeof(s.
