import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8()
    y = ctypes.c_uint16()
    _pack_ = 1

s = S()
print(ctypes.sizeof(s))

print(ctypes.sizeof(s.x))
print(ctypes.sizeof(s.y))

s.x = 0x11
s.y = 0x2233

print(s.x)
print(s.y)

