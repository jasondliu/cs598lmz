import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Field(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return getattr(obj.contents, self.name)

    def __set__(self, obj, value):
        setattr(obj.contents, self.name, value)

def _make_field(field):
    return Field(field[0], field[1])

def _make_fields(fields):
    return map(_make_field, fields)

class Structure(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super(Structure, self).__init__(*args, **kwargs)
        for field in _make_fields(self._fields_):
            setattr(self, field.name, field.__get__(self, self.__class__))

    def __setattr__(self, name, value):
        if hasattr(self,
