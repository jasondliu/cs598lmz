import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

s = S()
s.x = 1
s.y = 2
s.z = 3
print(s.x, s.y, s.z)

s = S(1, 2, 3)
print(s.x, s.y, s.z)

s = S(*[1, 2, 3])
print(s.x, s.y, s.z)

s = S(**{"x": 1, "y": 2, "z": 3})
print(s.x, s.y, s.z)

s = S(**{"x": 1, "y": 2, "z": 3, "w": 4})
print(s.x, s.y, s.z)

class S(ctypes.Structure):
    _fields
