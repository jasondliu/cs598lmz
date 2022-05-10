import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class from_buffer(object):
    __slots__ = ['_obj']

    def __init__(self, obj):
        self._obj = obj
    def __getattribute__(self, name):
        if name == '_obj':
            return object.__getattribute__(self, name)
        return getattr(self._obj, name)

class CField(from_buffer):
    def __init__(self, obj, offset):
        self._obj = obj
        self._offset = offset

class CStruct(ctypes.Structure):
    def __getattribute__(self, name):
        if name in self._fields_:
            offset = self._fields_[name][1]
            return CField(self, offset)
        return ctypes.Structure.__getattribute__(self, name)

    @classmethod
    def from_param(cls, obj):
        if isinstance(obj, ctypes.Structure):
            return cls.from_buffer(obj)
        else:
            return cls.from_address(obj
