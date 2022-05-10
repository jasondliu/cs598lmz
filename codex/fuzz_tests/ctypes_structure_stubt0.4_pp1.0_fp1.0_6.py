import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

s = S()
print s.x
print s.y
s.x = 3
print s.x
print s.y
print s
print s.__dict__
print s.__class__
print s.__class__.__dict__
print S.__dict__
print S.__class__
print S.__class__.__dict__
print S.__class__.__bases__
print S.__class__.__bases__[0].__dict__
print S.__class__.__bases__[0].__bases__
print S.__class__.__bases__[0].__bases__[0].__dict__
print S.__class__.__bases__[0].__bases__[0].__bases__
print S.__class__.__bases__[0
