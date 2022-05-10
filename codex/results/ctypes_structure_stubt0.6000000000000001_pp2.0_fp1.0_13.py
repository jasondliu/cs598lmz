import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
print s.x
s.x = 10
print s.x

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s = S()
print s.x
s.x = 10
print s.x

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
print s.x, s.y
s.x = 10
s.y = 20
print s.x, s.y

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
print s.x, s.y
s.x = 10
s.y = 20
print s.x, s.y
print s.__getattribute__('x'), s.__getattribute__('y')
print s.__getattribute__('
