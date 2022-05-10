import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    def __repr__(self):
        return 'S(%r, %r, %r)' % (self.x, self.y, self.z)

s = S()
s.x = 1
s.y = 2
s.z = 3

print s

print 'x:', s.x
print 'y:', s.y
print 'z:', s.z

print 'sizeof(s):', ctypes.sizeof(s)
print 's.x:', s.x
print 's.y:', s.y
print 's.z:', s.z

s.x = 10
s.y = 20
s.z = 30

print 'sizeof(s):', ctypes.sizeof(s)
print 's.x:', s.x
print 's.y:', s.y
print 's.z:', s.z

#print 's.x:', s.x
