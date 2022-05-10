import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("foo", ctypes.c_int)]

s = S()
s.foo = s.x
print s.foo
s.foo = s.x * 3
s.x = 3
print s.foo
