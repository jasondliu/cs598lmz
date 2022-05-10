import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class descr(object):
    def __init__(self, name, cls, offset):
        self.name = name
        self.cls = cls
        self.offset = offset
    def __get__(self, obj, cls):
        if obj is None:
            return self.cls
        return self.cls.from_address(id(obj) + self.offset)

def to_c_struct(cls):
    class C(ctypes.Structure):
        _fields_ = [(name, ctypes.CField) for name, attr in cls.__dict__.items() if type(attr) is descr]
    return C

def field(cls):
    if issubclass(cls, ctypes.Structure):
        return descr(cls.__name__, cls, 0)
    return descr(cls.__name__, ctypes.c_int, 0)

class Point(object):
    x = field(ctypes.c_int)
    y = field(ctypes.
