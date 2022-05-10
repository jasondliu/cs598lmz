import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulonglong()
    y = ctypes.c_ulonglong()
    z = ctypes.c_ulonglong()

s = S()
print(s)

s.x = 0x1234567800000000
s.y = 0x8765432100000000
s.z = 0x1111111111111111

print(s)

print(hex(s.x))
print(hex(s.y))
print(hex(s.z))

print(s.x)
print(s.y)
print(s.z)

s.x = 0x12345678
s.y = 0x87654321
s.z = 0x1111111111111111

print(s.x)
print(s.y)
print(s.z)

print(hex(s.x))
print(hex(s.y))
print(hex(s.z))

print(s)

