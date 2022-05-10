import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class fieldtypechecker(object):
    __slots__ = 'ctype', 'ofs'

    def __init__(self, ctype, ofs):
        self.ctype, self.ofs = ctype, ofs

    def __call__(self, typ, value):
        if isinstance(value, self.ctype):
            return True
        name = getattr(self.ctype, '__name__', str(self.ctype))

        if type(value) is self.ctype:
            return True
        raise TypeError('a %s is required' % name)

def _ctypes_simple_instance(cls):
    """Inline ctypes_simple_instance()."""
    class _cls(cls):
        _type_ = cls
        _fields_ = []

        def __repr__(self):
            return '%s.%s()' % (cls.__module__, cls.__name__)
    return _cls()

class Structure(ctypes.Structure):
    """St
