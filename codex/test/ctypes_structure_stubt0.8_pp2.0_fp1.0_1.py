import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

    def __str__(self):
        return "S(%r, %r)" % (self.x, self.y)

    def __repr__(self):
        return str(self)

