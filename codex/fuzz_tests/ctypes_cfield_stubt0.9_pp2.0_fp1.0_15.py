import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    """
    A special ctypes integer type that allows to specify the base of the
    string representation using a format string in __repr__.
    """

    def __repr__(self):
        return self.base_format % (self.base, self.value)

class Dummy(ctypes.Structure):
    _fields_ = [
        ('x0', ctypes.c_int, 5),
        ('x1', ctypes.c_int, 27),
        ('x2', ctypes.c_int, 5),
    ]
    x = CField(8)

class ArraySample(ctypes.Structure):
    _fields_ = [('a', ctypes.POINTER(ctypes.c_int)), ('b', ctypes.c_int)]

def strip_type_repr(value):
    return repr(value).replace('<type', '<_type').replace('class ', '')

def get_ctypes_type(value):
    typerepr = strip_type_re
