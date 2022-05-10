import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    def __repr__(self):
        return 'S(%r, %r, %r)' % (self.x, self.y, self.z)

s = S()
s.x = 1
s.y = 2
s.z = 3

