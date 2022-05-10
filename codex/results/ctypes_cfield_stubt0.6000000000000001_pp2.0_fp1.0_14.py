import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class PyField(ctypes.CField):
    def __init__(self, name, type, offset, size):
        self._name = name
        self._type = type
        self._offset = offset
        self._size = size

    def __getattribute__(self, attr):
        #print 'getattr', attr
        if attr == '_name':
            return self.__dict__['_name']
        elif attr == '_type':
            return self.__dict__['_type']
        elif attr == '_offset':
            return self.__dict__['_offset']
        elif attr == '_size':
            return self.__dict__['_size']
        elif attr == '__dict__':
            return self.__dict__
        elif attr in self.__dict__:
            return self.__dict__[attr]
        else:
            return getattr(self._type, attr)

    def __setattr__(self, attr, value):
        if attr in self.
