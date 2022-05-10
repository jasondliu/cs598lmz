import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.CField):
    def __init__(self, doc, type_):
        ctypes.CField.__init__(self, doc, type_)
    def _get_name(self):
        return "c_int"
    def _get_offset(self):
        return 0
    def _get_type(self):
        return ctypes.c_int
    def _get_size(self):
        return 4
    name = property(_get_name)
    offset = property(_get_offset)
    type = property(_get_type)
    size = property(_get_size)

def mutate_fields(cls):
    print cls._fields_
    cls._fields_ = [(f[0], X(f[0], f[1])) for f in cls._fields_]
    print cls._fields_
    cls._pack_ = 1

old_new_class = type.__new__

def my_new_class(cls, name, bases, dct):
    if dct
