import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint
    _fields_ = [("x", ctypes.c_uint)]

s = S()

b = memoryview(s)

print(b.format)
print(b.itemsize)
print(b.shape)
print(b.strides)

b[0] = 1
print(b[0])
print(s.x)

b[0] = 2
print(b[0])
print(s.x)

b[0] = -1
print(b[0])
print(s.x)

b[0] = -2
print(b[0])
print(s.x)

b[0] = 2**32
print(b[0])
print(s.x)

b[0] = -2**32
print(b[0])
print(s.x)

b[0] = 2**33
print(b[0])
print(s.x)

b[0] = -2**33
print(b[0])
print(s.
