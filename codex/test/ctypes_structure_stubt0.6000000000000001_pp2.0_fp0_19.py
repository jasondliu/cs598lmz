import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

    def __str__(self):
        return 'x=%d, y=%d' % (self.x, self.y)

class T(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

    def __str__(self):
        return 'x=%d, y=%d' % (self.x, self.y)

