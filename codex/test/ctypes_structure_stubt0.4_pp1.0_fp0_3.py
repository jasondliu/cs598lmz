import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    def __str__(self):
        return 'S(%d)' % self.x

class T(ctypes.Structure):
    _fields_ = [("s", S)]

a = T()
a.s.x = 42
