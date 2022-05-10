import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CAPIField(ctypes.CField, object):
    """
    This class is used to define C API fields in C structures.

    This is a base class, that can be specialized with a type.
    """

    def __init__(self, name, type_=None):
        self.name = name
        self._type = type_

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, self.name)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self._type(obj, self.name)

    def __set__(self, obj, value):
        self._type(obj, self.name).value = value

    def __delete__(self, obj):
        raise AttributeError("can't delete attribute")

class CField(ctypes.CField, object):
    """
    This class is used to define C fields in C structures.

    This is a base class, that can be specialized with a type
