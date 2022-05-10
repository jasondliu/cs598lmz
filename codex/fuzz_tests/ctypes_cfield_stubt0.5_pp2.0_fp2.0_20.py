import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, name, type, offset):
        self.name = name
        self.type = type
        self.offset = offset
        self.size = ctypes.sizeof(type)

    def __repr__(self):
        return '%s(%r, %r, %r)' % (self.__class__.__name__, self.name, self.type, self.offset)

class CStruct(ctypes.Structure):
    _fields_ = []

    @classmethod
    def from_ctypes_struct(cls, ctypes_struct):
        fields = []
        offset = 0
        for name, type in ctypes_struct._fields_:
            fields.append(CField(name, type, offset))
            offset += ctypes.sizeof(type)
        cls._fields_ = fields
        return cls

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._fields
