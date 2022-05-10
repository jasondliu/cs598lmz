import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2
print s.x, s.y

s2 = S()
s2.x = 3
s2.y = 4
print s2.x, s2.y

s.x = 5
s.y = 6
print s.x, s.y
print s2.x, s2.y

s3 = S()
s3.x = 7
s3.y = 8
print s3.x, s3.y
print s.x, s.y
print s2.x, s2.y

s4 = S()
s4.x = 9
s4.y = 10
print s4.x, s4.y
print s3.x, s3.y
print s.x, s.y
print s2.x, s2.y

s5 = S()
s5.x = 11
s5.y = 12
print s5.x, s5.y
