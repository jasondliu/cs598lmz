import ctypes

class S(ctypes.Structure):
    x = 1
    y = 2

s = S()
print s.x
s.z = 3
s.x = 5
s.y = 4
print s.x
print s.z
print s.y
print 

s = S()
print dir(s)
p
