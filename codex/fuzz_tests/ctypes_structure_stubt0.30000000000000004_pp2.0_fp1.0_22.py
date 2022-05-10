import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x
print s.y

print s
print s.__dict__
print s.x.__dict__
print s.y.__dict__
