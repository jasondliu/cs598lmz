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

s4 = S(s3)
print(s4.x, s4.y)

s5 = S(*(7, 8))
print(s5.x, s5.y)

s6 = S(**{'x': 9, 'y': 10})
print(s6.x, s6.y)

s7 = S(s6)
print(s7.x, s7.y)

s8 = S(**s7._asdict())
print(s8.x, s8.y)

s9 = S(**s8._asdict())
print(s9.x, s9.y)
