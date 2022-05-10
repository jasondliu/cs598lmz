import ctypes
ctypes.cast(0, ctypes.py_object).value

# From the ctypes docs
# http://docs.python.org/library/ctypes.html#ctypes._Pointer.from_buffer
class POINTER(object):
    def __init__(self, type):
        self.type = type

    def from_param(self, param):
        typ = type(param)
        if typ is self.type:
            return param
        if isinstance(param, ctypes.Array):
            return param
        if isinstance(param, ctypes.py_object):
            return param
        if isinstance(param, ctypes._Pointer):
            return param
        if isinstance(param, int):
            return self.type.from_param(param)
        if hasattr(param, '_as_parameter_'):
            return self.type.from_param(param._as_parameter_)
        if isinstance(param, tuple):
            return self.type(*param)
        raise TypeError(
            "Can't convert %s" % (param.__class__
