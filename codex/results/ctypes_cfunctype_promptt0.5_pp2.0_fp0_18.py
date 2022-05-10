import ctypes
# Test ctypes.CFUNCTYPE
@CFUNCTYPE(c_int, c_int, c_int)
def my_add(a, b):
    return a + b
print(my_add(1, 2))

# Test ctypes.POINTER
class POINTER(object):
    def __init__(self, type):
        self.type = type
    def from_param(self, param):
        typename = param.__class__.__name__
        if hasattr(self.type, 'from_param'):
            return self.type.from_param(param)
        elif typename in ('SwigPyObject', 'SwigPyIterator'):
            return param
        else:
            return ctypes.cast(param, ctypes.POINTER(self.type))

class SwigPyObject(object):
    """
    This class is used to wrap a C pointer to a Python object.
    """
    def __init__(self, this):
        self.this = this
    def __repr__(self):
        return "<Swig Object of type '%s
