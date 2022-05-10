import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32
    z = ctypes.c_uint32
    w = ctypes.c_uint32

a = S()
b = S()

a.x = 0x12345678
a.y = 0x23456789
a.z = 0x34567890
a.w = 0x45678901

b.x = 0x56789012
b.y = 0x67890123
b.z = 0x78901234
b.w = 0x89012345

print(a.x)
print(a.y)
print(a.z)
print(a.w)

print(b.x)
print(b.y)
print(b.z)
print(b.w)
