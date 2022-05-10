import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def memo(f):
    class MemoDict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return MemoDict().__getitem__

def is_pointer_to(TP):
    return lambda tp: tp.__name__.startswith('LP_') and tp._type_ == TP

@memo
def _get_ctype(tp):
    if not issubclass(tp, ctypes._SimpleCData):
        return 'void'
    elif issubclass(tp, ctypes.c_int):
        return 'c_int'
    elif issubclass(tp, ctypes.c_uint):
        return 'c_uint'
    elif issubclass(tp, ctypes.c_long):
        return 'c_long'
    elif issubclass(tp, ctypes.c_ulong):
        return 'c_ulong'
    elif issubclass(tp, ctypes.c_longlong):
