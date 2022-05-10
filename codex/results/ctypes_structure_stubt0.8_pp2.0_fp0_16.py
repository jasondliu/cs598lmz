import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_float),
                ('y', ctypes.c_float)]

s1 = S()
s1.x = 4.6
s1.y = 3.2
print s1.x
print s1.y

s2 = S(4.6, 3.2)
print s2.x
print s2.y

d1 = D()
d1.x = 4.6
d1.y = 3.2
print d1.x
print d1.y

d2 = D(4.6, 3.2)
print d2.x
print d2.y

d3 = D(x=4.6, y=3.2)
print d3.x
print d3.y

print

# Test pointer fields.
class P(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.c
