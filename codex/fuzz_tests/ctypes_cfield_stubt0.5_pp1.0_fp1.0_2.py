import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(object):
    __slots__ = ['_name', '_ctype', '_offset', '_index']
    def __init__(self, name, ctype, offset, index):
        self._name = name
        self._ctype = ctype
        self._offset = offset
        self._index = index
    def __get__(self, obj, cls):
        if obj is None:
            return self
        return obj._objects[self._index]
    def __set__(self, obj, value):
        obj._objects[self._index] = value
    def __delete__(self, obj):
        raise AttributeError("can't delete attribute")
    def __repr__(self):
        return "<CField '%s'>" % (self._name,)
    def from_address(self, address):
        return self.__get__(obj, cls)

class CStructure(object):
    __slots__ = ['_objects', '_fields_']
    def __init__(self):
        self._objects
