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
s3.x = 7
s3.y = 8
s3.z = 9

print(s3.x, s3.y, s3.z)

s4 = S()
s4.x = 10
s4.y = 11
s4.z = 12

print(s4.x, s4.y, s4.z)

s5 = S()
s5.x = 13
s5.y = 14
s5.z = 15

print(s5.x, s5.y, s5.z)

