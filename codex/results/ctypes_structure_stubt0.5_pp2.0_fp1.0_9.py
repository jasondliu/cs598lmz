import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class T(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def f(a, b, c):
    return a + b + c

#
# test with builtin types
#

print f(1, 2, 3)
print f(*(1, 2, 3))
print f(*[1, 2, 3])
print f(*(i for i in xrange(1, 4)))
print f(*(i for i in xrange(1, 4)))

#
# test with ctypes types
#

s = S(1, 2, 3)
print f(s.x, s.y, s.z)
print f(*s)
print f(*[s.x, s.y, s.z])
print f(*(s.x, s.y, s.z))
print f(*(i for i in s
