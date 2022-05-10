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

s2 = S(4, 5, 6)
print(s2.x, s2.y, s2.z)

s3 = S(x=7, y=8, z=9)
print(s3.x, s3.y, s3.z)

s4 = S(x=10)
print(s4.x, s4.y, s4.z)

s5 = S(x=11, y=12)
print(s5.x, s5.y, s5.z)

s6 = S(x=13, z=14)
print(s6.x, s6.y, s6.z)

s7 = S(z=15)
print(s7.x, s7.y, s7
