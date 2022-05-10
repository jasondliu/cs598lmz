import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFunctionType(type):
    def __init__(self, name, bases, dct):
        self._flags_ = dct.pop('_flags_', FUNCFLAG_CDECL)
        self._restype_ = dct.pop('_restype_', ctypes.c_int)
        self._argtypes_ = dct.pop('_argtypes_', None)
        self._errcheck_ = dct.pop('_errcheck_', None)
        self._name_ = dct.pop('_name_', None)
        self._dll_ = dct.pop('_dll_', None)

        super(CFunctionType, self).__init__(name, bases, dct)

    def __call__(self, *args, **kw):
        return self._call_(*args, **kw)

    def _call_(self, *args, **kw):
        func = self._create_()
        return func(*args, **kw)

    def _create_(self):
        func = getattr(self, '_func_', None
