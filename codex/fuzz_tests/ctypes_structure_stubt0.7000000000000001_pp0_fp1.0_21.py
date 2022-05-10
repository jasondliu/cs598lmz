import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('y', ctypes.c_long), ('z', ctypes.c_double)]

print S()
print S(x=1, y=2, z=3.0)
print S(1, 2, 3.0)
print S([1, 2, 3.0])
print S(*[1, 2, 3.0])
print S(**{'x': 1, 'y': 2, 'z': 3.0})

print S(1, 2)

try:
    print S(1, 2, 3, 4)
except TypeError:
    print 'TypeError'

try:
    print S(1, 2, 3, 4, 5)
except TypeError:
    print 'TypeError'

try:
    print S()[1]
except TypeError:
    print 'TypeError'
