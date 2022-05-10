import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyDescr(object):
    __slots__ = ['name', 'field']

    def __init__(self, name, field):
        self.name = name
        self.field = field

    def set_field(self, obj, value):
        setattr(obj, self.name, value)

    def get_field(self, obj):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        print "__set__", obj, value, self.field
        #self.field.restype = ctypes.c_int
        self.field.restype = type(value)
        #self.field(obj, ctypes.py_object(value))
        self.field(obj, value)

    def __get__(self, obj, type=None):
        print "__get__", obj, type, self.field
        self.field.restype = ctypes.c_int
        res = self.field(obj, -1)
        #self.field.restype = type(res)
