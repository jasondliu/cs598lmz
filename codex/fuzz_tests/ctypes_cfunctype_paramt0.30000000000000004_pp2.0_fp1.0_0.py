import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def callback(f):
    """
    Decorator to convert a function into a callback function.
    """
    f._as_parameter_ = FUNTYPE(f)
    return f

class _CStruct(ctypes.Structure):
    """
    Base class for all structures.
    """
    def __str__(self):
        return '\n'.join(['%s: %s' % (field, getattr(self, field))
                          for field, _ in self._fields_])

class _CStructPtr(_CStruct):
    """
    Base class for all structures that are pointers.
    """
    _type_ = None
    _pointer_ = ctypes.POINTER(_type_)

    def __init__(self, ptr):
        assert isinstance(ptr, ctypes.c_void_p)
        self._as_parameter_ = self._pointer_(ptr)

    def __str__(self):
        return '%s\n%s' % (self._type_, super(_CStructPtr, self).__str
