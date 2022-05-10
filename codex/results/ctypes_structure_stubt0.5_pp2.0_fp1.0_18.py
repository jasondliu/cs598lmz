import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x
print s.y

print s.x + s.y

print s
print ctypes.sizeof(s)

print s.__dict__
print s._fields_

print ctypes.sizeof(s.x)
