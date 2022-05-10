import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __get__(self, obj, cls):
        print "get", obj, cls

S.x = CField()

s = S()
print s.x
