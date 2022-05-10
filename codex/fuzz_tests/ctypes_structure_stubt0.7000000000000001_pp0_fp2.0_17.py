import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_char()
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_char)
    ]

s = S()
print '%s' % s.y
print '%s' % s.x
print s._fields_
print S.__dict__
print S.__bases__

print S.y
print S.x
print S.__dict__
print S.__bases__
