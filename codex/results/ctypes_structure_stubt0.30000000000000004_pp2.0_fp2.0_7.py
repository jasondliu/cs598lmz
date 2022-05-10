import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

s = S()
print s.x
print s.y

s.x = 1
s.y = 2

print s.x
print s.y

print s.__dict__

print s._fields_

print s._fields_[0]
print s._fields_[1]

print s._fields_[0][0]
print s._fields_[0][1]

print s._fields_[1][0]
print s._fields_[1][1]

print s._fields_[0][0] == 'x'
print s._fields_[0][1] == ctypes.c_int

print s._fields_[1][0] == 'y'
print s._fields_[1][1] == ctypes.c_int

print s._fields_[0][0] == 'x'

