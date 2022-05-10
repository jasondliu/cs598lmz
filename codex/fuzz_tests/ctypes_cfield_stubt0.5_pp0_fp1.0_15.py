import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, name, type_):
        super().__init__(name, type_)
        self.type = type_

    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.name, self.type)

class S(ctypes.Structure):
    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __setattr__(self, name, value):
        if name in self._fields_:
            field = self._fields_[name]
            if isinstance(field, CField):
                self.__setitem__(name, field.type(value))
            else:
                self.__setitem__(name, value)
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
