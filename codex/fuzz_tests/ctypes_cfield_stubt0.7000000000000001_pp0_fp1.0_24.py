import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFunctionType(object):
    """
    Encapsulates the data for a C function.

    """

    def __init__(self, ctype, paramflags, checker):
        self.ctype = ctype
        self.paramflags = paramflags
        self.checker = checker

    def __repr__(self):
        return '<CFunctionType %r %r %r>' % (
            self.ctype, self.paramflags, self.checker)

class CType(object):
    """
    Abstract base class for all C types.

    """
    __slots__ = ()

    # the _CData_cache entry for this type
    _CData_cache = None

    def from_param(self, value):
        """
        Convert the python object to a parameter object.

        """
        return value

    def _sizeofinstances(self):
        """
        Return the size of an instance of the object.

        """
        raise NotImplementedError

    def alignof(self):
        """
        Return the
