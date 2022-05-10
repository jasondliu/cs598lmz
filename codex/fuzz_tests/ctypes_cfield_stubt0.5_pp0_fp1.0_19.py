import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, name):
        self.name = name
    def __getattr__(self, name):
        if name == '_fields_':
            return [('f1', ctypes.CField), ('f2', ctypes.CField)]
        return getattr(self.__class__, name)

class D(C):
    _fields_ = [('f3', ctypes.CField), ('f4', ctypes.CField)]

class E(D):
    pass

print S._fields_
print C('C')._fields_
print D('D')._fields_
print E('E')._fields_
