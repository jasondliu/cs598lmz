import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFields(dict):
    def __setitem__(self, key, value):
        self._check_input(value)
        super(CFields, self).__setitem__(key, value)
    def update(self, E=None, **F):
        super(CFields, self).update(E, **F)
        self._check_input(E)
        self._check_input(F)
    def _check_input(self, value):
        if getattr(value, '_fields_', None):
            for t in value._fields_:
                self._check_input(t[1])
        if isinstance(value, ctypes.CField):
            self._check_recursion(value)
        if (   isinstance(value, type)
            and issubclass(value, ctypes.Array)
            and value._type_ is not ctypes.c_char):
            self._check_recursion(value._type_)
    def _check_recursion(self, value):
        if value in self:
           
