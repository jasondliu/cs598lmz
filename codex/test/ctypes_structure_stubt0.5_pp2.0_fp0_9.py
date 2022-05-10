import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    y = ctypes.c_uint8
    z = ctypes.c_uint8
    w = ctypes.c_uint8

s = S()
print(s.x)
print(s.y)
print(s.z)
print(s.w)

s.x = 2
s.y = 3
s.z = 4
s.w = 5

print(s.x)
print(s.y)
print(s.z)
print(s.w)

print(s.__dict__)

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint8),
                ("y", ctypes.c_uint8),
                ("z", ctypes.c_uint8),
                ("w", ctypes.c_uint8)]

s = S()
print(s.x)
print(s.y)
print(s.z)
print(s.w)

s.x = 2
s.y = 3
s
