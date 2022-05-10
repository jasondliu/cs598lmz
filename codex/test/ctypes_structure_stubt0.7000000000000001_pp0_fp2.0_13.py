import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_float

class B(ctypes.BigEndianStructure):
    x = ctypes.c_longlong
    y = ctypes.c_float

class L(ctypes.LittleEndianStructure):
    x = ctypes.c_longlong
    y = ctypes.c_float

print(ctypes.sizeof(S))
print(ctypes.sizeof(B))
print(ctypes.sizeof(L))

a = S()
a.x = 0x1122334455667788
a.y = 1.0

print(a.x)
print(a.y)

print(a)
print(bytearray(a))

b = B()
c = L()

print(b)
print(bytearray(b))
print(c)
print(bytearray(c))

