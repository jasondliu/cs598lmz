import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __get__(self, obj, cls):
        print "getting", self.name
        return getattr(obj, self.name)
    def __set__(self, obj, value):
        print "setting", self.name, value
        setattr(obj, self.name, value)

S._fields_ = [(n, CField(t)) for n, t in S._fields_]

s = S()
s.x = 42
print s.x
