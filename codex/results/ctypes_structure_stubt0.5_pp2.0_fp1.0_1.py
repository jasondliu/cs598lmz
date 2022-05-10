import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
print s.x, s.y, s.z
s.x = 1
s.y = 2
s.z = 3
print s.x, s.y, s.z

s = S(1,2,3)
print s.x, s.y, s.z

s = S(z=3,x=1,y=2)
print s.x, s.y, s.z

s = S(1,2)
print s.x, s.y, s.z

s = S(1)
print s.x, s.y, s.z

s = S(1, z=3)
print s.x, s.y, s.z

try:
    s = S(1,2,z=3)
except TypeError, details:
    print details

try:
    s = S(1,2,3,4)
except TypeError, details:
