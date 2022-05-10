import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print s.x, s.y
print repr(s)

print ctypes.addressof(s)
print s._fields_
print s.y.offset
print ctypes.addressof(s.y)
print ctypes.addressof(s.y) - ctypes.addressof(s)
print ctypes.addressof(s.y) - ctypes.addressof(s.x)
print ctypes.addressof(s.y) - ctypes.addressof(s.x) == s.y.offset
print ctypes.addressof(s.y) - ctypes.addressof(s) == s.y.offset

s.x = 5
s.y = 10
print s.x, s.y
print repr(s)

s = S(1, 2)
print s.x, s.y
print repr(s)

class S(ctypes.Structure):
    _fields_ =
