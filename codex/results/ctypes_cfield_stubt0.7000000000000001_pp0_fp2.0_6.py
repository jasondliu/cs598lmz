import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldType = type(S.x.type)

# This is used to do an extra check in the __new__ method of CFuncPtr.
def _check_func(func):
    if isinstance(func, ctypes.CFunctionType):
        return func
    else:
        raise TypeError(func)

def _CFuncPtr(name, argtypes, restype=None, errcheck=None):
    # XXX: This is a hack, there should be a cleaner way.
    module = sys._getframe(1).f_globals.get('__name__', '__main__')
    if module == '__main__':
        module = None
    return ctypes.CFUNCTYPE(restype, *argtypes,
                            _name=name, _errcheck=errcheck,
                            _aliased=True,
                            _checks=_check_func,
                            _module=module)

def _CFuncPtr_cdecl(name, argtypes, restype=None, errcheck=None):
    return _CFunc
