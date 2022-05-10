import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class U(ctypes.Union):
    x = ctypes.c_int
    y = ctypes.c_int

print 'S.x:', S.x
print 'S.x.offset:', S.x.offset
print 'S.x.size:', S.x.size
print 'U.x:', U.x
print 'U.x.offset:', U.x.offset
print 'U.x.size:', U.x.size
print 'U.y:', U.y
print 'U.y.offset:', U.y.offset
print 'U.y.size:', U.y.size
