import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

s2 = S(x=3, y=4)
print s2.x, s2.y

s3 = S(**{'x':5, 'y':6})
print s3.x, s3.y

s4 = S(**{'x':7, 'y':8, 'z':9})
print s4.x, s4.y

s5 = S(**{'x':10, 'y':11, 'z':12})
print s5.x, s5.y
