import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def obj_getattro(obj, attr):
    return getattr(obj, attr)

def make_descr(name, typ, setattro=None, getattro=obj_getattro):
    d = ctypes.Field(name, typ)
    d.__set__ = types.MethodType(setattro, d)
    d.__get__ = types.MethodType(getattro, d)
    return d


class D(object):
    def __init__(self, *args):
        self.args = args

class T(object):
    def __init__(self, *args):
        self.d = D(*args)

    def __getattribute__(self, attr):
        return getattr(object.__getattribute__(self, "d"), attr)

def make_obj(d, name, typ, setattro=None, getattro=obj_getattro):
    if setattro:
        setattr(d, name, make_descr(name, typ, setattro))
