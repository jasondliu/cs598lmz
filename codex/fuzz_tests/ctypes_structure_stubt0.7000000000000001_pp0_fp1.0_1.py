import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16()
    y = ctypes.c_uint16()

class T(ctypes.Structure):
    x = ctypes.c_uint16()
    y = ctypes.c_uint32()

s = S()
s.x = 0x1234
s.y = 0x5678

print(s.x, s.y)
print(ctypes.addressof(s.x), ctypes.addressof(s.y))
# s.y = 0x5678
# print(s.x)
# print(ctypes.addressof(s.y))
# print(type(s))

# t = T()
# print(t.y)
# print(ctypes.addressof(t.y))
# print(type(t))

# print(ctypes.addressof(s))
# print(ctypes.addressof(t))

# def set_struct(b, obj):
#     # print(ctypes.cast(ctypes.addressof(b), c
