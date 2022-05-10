import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)
print(s.__dict__)

s2 = S(1, 2, 3)
print(s2.x, s2.y, s2.z)
print(s2.__dict__)

s3 = S(x=1, y=2, z=3)
print(s3.x, s3.y, s3.z)
print(s3.__dict__)

s4 = S(**{'x':1, 'y':2, 'z':3})
print(s4.x, s4.y, s4.z)
print(s4.__dict__)

s5 = S(**dict(x=1, y=2, z=3))
print(s5.x, s5.y, s5.z)
