import ctypes
# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class PointArray(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', Point)]

pa = PointArray()
pa.a = 1
pa.b = 2
pa.c.x = 3
pa.c.y = 4

assert pa.c.x == 3
assert pa.c.y == 4

pa.c = Point(5, 6)
assert pa.c.x == 5
assert pa.c.y == 6

# Test ctypes.CField with pointers
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class PointArray(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', c
