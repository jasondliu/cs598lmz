import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class _type(type(ctypes._SimpleCData)):
    _type_ = "<class '_type'>"
    __module__ = 'ctypes'

    def _get_type_(to_cls):
        if issubclass(to_cls, ctypes._SimpleCData):
            return to_cls._type_
        elif issubclass(to_cls, ctypes.CField):
            return 'CField'
        return to_cls
    _get_type_ = staticmethod(_get_type_)

class _object(object):
    _type_ = "<class '_object'>"
    __module__ = 'ctypes'

class _object_with_bases(object):
    _type_ = "<class '_object_with_bases'>"
    __module__ = 'ctypes'
    __bases__ = ()

class _object_with_bases_and_slots(object):
    _type_ = "<class '_object_with_bases_and_slots'>"
    __module
