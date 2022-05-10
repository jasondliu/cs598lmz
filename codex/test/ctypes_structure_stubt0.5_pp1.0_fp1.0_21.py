import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("y", ctypes.c_int),
                ("z", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("a", S),
                ("b", S),
                ("c", S),
                ("d", S)]

t = T()
print(t.a.x)
print(t.a.y)
print(t.a.z)
print(t.b.x)
print(t.b.y)
print(t.b.z)
print(t.c.x)
print(t.c.y)
print(t.c.z)
print(t.d.x)
print(t.d.y)
print(t.d.z)

print(ctypes.sizeof(t))
print(ctypes.sizeof(t.a))
print(ctypes.sizeof(t.b))
print(ctypes.sizeof(t.c))
