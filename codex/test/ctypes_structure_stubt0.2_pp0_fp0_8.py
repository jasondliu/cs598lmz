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

s2 = S()
s2.x = 4
s2.y = 5
s2.z = 6

print(s2.x, s2.y, s2.z)

s3 = S()
s3.x = s.x
s3.y = s.y
s3.z = s.z

print(s3.x, s3.y, s3.z)

s4 = S()
s4.x = s2.x
s4.y = s2.y
s4.z = s2.z

print(s4.x, s4.y, s4.z)

s5 = S()
s5.x = s3.x
s5.y = s3.y
