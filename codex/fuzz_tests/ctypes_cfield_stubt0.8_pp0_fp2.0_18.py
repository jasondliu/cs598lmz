import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

"""
If you are using Python 2.7 or later, you can use a simple class instead:
class CField(object):
    _as_parameter_ = None
"""

class CFieldSubClass(ctypes.CField):
    # the only difference is that in __init__() the
    # instance is assigned to the _as_parameter_
    # attribute:
    def __init__(self, name, type, doc=None):
        self.name = name
        self.type = type
        self.__doc__ = doc
        self._as_parameter_ = self

# This is needed because we must have a subtype of the _ctypes.c_void_p
# class which points at the _ctypes.c_void_p instance which is the
# address of a buffer allocated by the C library:
class CPointer(ctypes.c_void_p):
    def __init__(self, addr):
        super(CPointer, self).__init__(addr)
        self.addr = self.value

# Create a ctypes.
