import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble
    y = ctypes.c_int
    z = ctypes.c_longdouble
    _fields_ = ('x', 'y', 'z')

class S2(ctypes.Structure):
    x = ctypes.c_longdouble
    y = ctypes.c_int
    z = ctypes.c_longdouble
    _fields_ = ('x', 'z', 'y')

addresses = {}

def addr(o):
    if id(o) not in addresses:
        addresses[id(o)] = id(o)
    return addresses[id(o)]

s = S()
print(s.x == s.z)
s.x = 1.23
s.y = 42
s.z = 2.46
print(s.x == s.z)
s.x = 2.46
s.y = 43
s.z = 4.92
print(s.x == s.z)
print(addr(s.x), addr(s.z))

s2 = S2()

