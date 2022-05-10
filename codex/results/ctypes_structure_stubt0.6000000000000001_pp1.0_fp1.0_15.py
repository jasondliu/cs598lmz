import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print s.x, s.y
s.x = 1
s.y = 2
print s.x, s.y

s2 = S(x=10, y=20)
print s2.x, s2.y
s2.x = 11
s2.y = 12
print s2.x, s2.y

s3 = S(x=100)
print s3.x, s3.y

# s4 = S(x=1000, z=2000) # error
# print s4.x, s4.y

s5 = S()
print s5.x, s5.y
s5.x = 10
s5.y = 20
print s5.x, s5.y
s5.z = 100
print s5.z

s6 = S()
print s6.x, s6.y
s6.x = 10
s6.y = 20
print s6.x, s6.y

