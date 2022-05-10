import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print 's.x = %d, s.y = %d' % (s.x, s.y)

s1 = S()
s1.x = 3
s1.y = 4

print 's1.x = %d, s1.y = %d' % (s1.x, s1.y)
