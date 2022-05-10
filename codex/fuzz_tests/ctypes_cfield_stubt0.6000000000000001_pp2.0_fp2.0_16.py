import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Type(object):
    """
    Descriptor for a C type
    """
    _cache = {}

    def __init__(self, name, size, alignment):
        self.name = name
        self.size = size
        self.alignment = alignment

    def __repr__(self):
        return "<ctypes.Type %s>" % (self.name,)

    def __hash__(self):
        return hash((self.__class__, self.name, self.size, self.alignment))

    def __eq__(self, other):
        if not isinstance(other, Type):
            return NotImplemented
        return self.name == other.name and\
               self.size == other.size and\
               self.alignment == other.alignment

    def __ne__(self, other):
        if not isinstance(other, Type):
            return NotImplemented
        return not (self == other)

    @staticmethod
    def from_param(param):
        if isinstance(param, Type):
            return param

