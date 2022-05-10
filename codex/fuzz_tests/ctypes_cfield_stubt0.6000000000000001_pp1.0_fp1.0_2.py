import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFunctionType(type):
    _cache = {}
    def __new__(cls, name, bases, dct):
        if '_restype_' in dct:
            dct['_restype_'] = ctypes._get_ctypes_type(dct['_restype_'])
        if '_argtypes_' in dct:
            dct['_argtypes_'] = [ctypes._get_ctypes_type(arg) for arg in dct['_argtypes_']]
        return type.__new__(cls, name, bases, dct)

    def __call__(cls, *args):
        if args in cls._cache:
            return cls._cache[args]
        else:
            obj = type.__call__(cls, *args)
            cls._cache[args] = obj
            return obj

class CFunction(object):
    __metaclass__ = CFunctionType
    _argtypes_ = []
    _restype_ = ctypes.c_int
    _flags
