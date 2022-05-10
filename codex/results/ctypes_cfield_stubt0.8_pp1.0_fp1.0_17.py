import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFieldObject:
    def __init__(self, obj, value):
        self._obj = obj
        self._value = value

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._value)

    def __get__(self, obj, cls):
        if obj is None:
            return self
        return self._value.__get__(obj, cls)

    def __set__(self, obj, value):
        return self._value.__set__(obj, value)

    def _getvalue(self, obj):
        return self._value.__get__(obj, type(obj))
    def _setvalue(self, obj, value):
        return self._value.__set__(obj, value)

class _CField_output(CFieldObject):
    def __init__(self, obj, value, doc=None):
        CFieldObject.__init__(self, obj, value)
        self.__doc__ = doc

class _C
