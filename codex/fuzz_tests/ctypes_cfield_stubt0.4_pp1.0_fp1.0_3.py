import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, **kwds):
        for k, v in kwds.items():
            setattr(self, k, v)
    def __repr__(self):
        return 'C(%s)' % ', '.join('%s=%r' % (k, v) for k, v in self.__dict__.items())

class CField(object):
    def __init__(self, name, type, offset):
        self.name = name
        self.type = type
        self.offset = offset
    def __get__(self, obj, cls):
        if obj is None:
            return self
        return getattr(obj, self.name)
    def __set__(self, obj, value):
        setattr(obj, self.name, value)

def make_ctypes_compatible(C):
    fields = []
    for k, t in C.__annotations__.items():
        if isinstance(t, ctypes.CField):
            fields.append((k,
