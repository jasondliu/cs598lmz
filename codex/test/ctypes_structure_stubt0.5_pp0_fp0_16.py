import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong
    z = ctypes.c_longlong

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x)
print(s.y)
print(s.z)

s.x = 4
s.y = 5
s.z = 6

print(s.x)
print(s.y)
print(s.z)

print(ctypes.sizeof(S))

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_longlong), ("y", ctypes.c_longlong), ("z", ctypes.c_longlong)]

s2 = S2()
s2.x = 1
s2.y = 2
s2.z = 3

print(s2.x)
print(s2.y)
print(s2.z)

s2.x = 4
s2.y = 5
