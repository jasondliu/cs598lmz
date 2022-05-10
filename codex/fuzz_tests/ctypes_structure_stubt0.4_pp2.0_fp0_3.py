import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x)
print(s.y)
print(s.z)
print(s.__sizeof__())

# ctypes.addressof(s)

a = ctypes.c_int(1)
# ctypes.addressof(a)

# ctypes.pointer(a)

# ctypes.pointer(s)

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int), ("z", ctypes.c_int)]

s2 = S2()
s2.x = 1
s2.y = 2
s2.z = 3

print(s2.x)
print(s2.y)
print(s2.z)
print(s2.__sizeof__())

#
