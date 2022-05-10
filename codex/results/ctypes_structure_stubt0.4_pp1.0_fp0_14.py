import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

class P(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

p = P()
p.x = 1
p.y = 2
p.z = 3

print(s)
print(p)

print(s.x)
print(p.x)

print(s.y)
print(p.y)

print(s.z)
print(p.z)

print(type(s))
print(type(p))

print(type(s.x))
print(type(p.x))

print(type(s.y))
print(type(p.y))

print(type(s.z))
print(type(p.z))

