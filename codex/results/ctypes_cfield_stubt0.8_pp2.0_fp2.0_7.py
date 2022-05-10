import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class StructField(ctypes.Field):
    __slots__ = ('ctype', 'offset')

    def __new__(cls, name, ctype, offset):
        obj = super(StructField, cls).__new__(cls, name)
        obj.ctype = ctype
        obj.offset = offset
        return obj

    def __repr__(self):
        return "StructField('%s', %r, %r)" % (self.name, self.ctype, self.offset)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return ctypes.c_void_p.from_buffer(obj, self.offset).value

    def __set__(self, obj, value):
        ctypes.c_void_p.from_buffer(obj, self.offset).value = value

class UnionField(ctypes.Field):
    __slots__ = ('ctype', 'offset')

    def __new__(cls, name, ctype, offset):
       
