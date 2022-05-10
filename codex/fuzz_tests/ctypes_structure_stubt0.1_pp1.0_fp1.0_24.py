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

s4 = S(z=10, y=11, x=12)
print(s4.x, s4.y, s4.z)

s5 = S(z=13)
print(s5.x, s5.y, s5.z)

s6 = S(z=14, x=15)
print(s6.x, s6.y, s6.z)

s7 = S(z=16, x=17, y=18)
print(
