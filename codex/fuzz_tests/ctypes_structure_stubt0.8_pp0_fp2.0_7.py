import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(5)
    _fields_ = [('y', ctypes.c_int, (x >= 0) * 31)]
    # XXX this code should not be needed:
    y = property(lambda self: (self.y & (2**(self.x - 1) - 1)) - 2**(self.x - 2))

class T(Structure):
    x = c_int(5)
    _fields_ = [('y', c_int, (x >= 0) * 31)]
    # XXX this code should not be needed:
    y = property(lambda self: (self.y & (2**(self.x - 1) - 1)) - 2**(self.x - 2))

print S().y
print T().y
