import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 10
s.y = 20

print(s.x)
print(s.y)

print(s.__dict__)
print(s._fields_)

print(ctypes.sizeof(s))
print(ctypes.sizeof(ctypes.c_int))
print(ctypes.sizeof(ctypes.c_char))

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s2 = S2()
s2.x = 10
s2.y = 20

print(s2.x)
print(s2.y)

print(s2.__dict__)
print(s2._fields_)

print(ctypes.sizeof(s2))
print(ctypes.sizeof(ctypes.c_int))
print(ctypes.sizeof(ctypes.c_char))

