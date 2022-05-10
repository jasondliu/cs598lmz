import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

c = C(1)

class CField(ctypes.CField):
    def __init__(self, name, *a, **kw):
        ctypes.CField.__init__(self, name, *a, **kw)
        self.name = name
    def __get__(self, obj, type=None):
        return getattr(obj, self.name)
    def __set__(self, obj, val):
        setattr(obj, self.name, val)

class CS(ctypes.Structure):
    _fields_ = [('x', CField(None, ctypes.c_int))]

cs = CS.from_address(id(c))
cs.x
cs.x = 2
cs.x
c.x
c.x = 3
cs.x
