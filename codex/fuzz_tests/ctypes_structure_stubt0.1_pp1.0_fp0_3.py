import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

s2 = S(3, 4)
print(s2.x, s2.y)

s3 = S(x=5, y=6)
print(s3.x, s3.y)

s4 = S(y=7, x=8)
print(s4.x, s4.y)

s5 = S(s4)
print(s5.x, s5.y)

s6 = S(*s4)
print(s6.x, s6.y)

s7 = S(**s4)
print(s7.x, s7.y)

s8 = S(s4, x=9)
print(s8.x, s8.y)

s9 = S(s4, y=10)
print(s9.x, s9.y)

s10 =
