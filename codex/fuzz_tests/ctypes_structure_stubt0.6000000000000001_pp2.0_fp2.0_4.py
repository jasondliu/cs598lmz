import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)

s = S()
s.x = 100
print(s.x)
print(ctypes.addressof(s.x))
print(ctypes.addressof(s))
print(ctypes.addressof(s.x) - ctypes.addressof(s))

s.y = 200
print(s.y)

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

s = S()
s.x = 100
print(s.x)
print(ctypes.addressof(s.x))
print(ctypes.addressof(s))
print(ctypes.addressof(s.x) - ctypes.addressof(s))

s.y = 200
print(s.y)
print(ctypes.addressof(s.y))



class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int
