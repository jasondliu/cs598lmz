import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [
        ('y', ctypes.c_int, 1),
        ('z', (ctypes.c_int, 2)),
    ]

s = S()
print 'x', s.x
print 'y', s.y
print 'z', s.z

s.x += 100
print type(s.x), s.x
s.y = -1
print 'y', s.y
s.z = 255
print 'z', s.z
