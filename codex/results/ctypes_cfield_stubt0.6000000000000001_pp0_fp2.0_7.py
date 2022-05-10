import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(object):
    __slots__ = ['_type_', '_offset_', '_name_']
    def __init__(self, type_, offset, name):
        self._type_ = type_
        self._offset_ = offset
        self._name_ = name
    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return obj._buffer_[self._offset_:][0]
    def __set__(self, obj, value):
        obj._buffer_[self._offset_:][0] = value

class CStruct(object):
    __slots__ = ['_buffer_', '_fields_']
    def __init__(self, fields_):
        self._fields_ = fields_
        self._buffer_ = bytearray(sum(f._type_.size for f in fields_))

def cstruct(cls, fields):
    fields_ = []
    offset = 0
    for name, type_ in fields:
        fields_.append(CField(type
