import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)
    ]

class S2(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)
    ]

    x = ctypes.c_int
    y = ctypes.c_int

print(S.x)
print(S2.x)

s = S()
print(s.x)
print(s.y)

s2 = S2()
print(s2.x)
print(s2.y)

s.x = 1
s.y = 2

print(s.x)
print(s.y)

s2.x = 1
s2.y = 2

print(s2.x)
print(s2.y)

print(S.x)
print(S2.x)
