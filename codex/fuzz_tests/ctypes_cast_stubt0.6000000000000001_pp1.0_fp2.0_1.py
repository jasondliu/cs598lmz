import ctypes
ctypes.cast(13.24, ctypes.c_int)

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]

p = Point(1, 2)
ctypes.cast(p, ctypes.c_int)

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]
    def __repr__(self):
        return 'Point(%g, %g)' % (self.x, self.y)

p = Point(1, 2)
ctypes.cast(p, ctypes.c_int)

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]
    def __repr__(self):
        return 'Point(%g, %g)' % (self.x, self.y)
    def __str__(self):
        return 'Point(%
