import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
del S

class COpaquePointer(object):
    """
    Subclass from a ctypes object
    """
    _is_opaque_pointer = True

    def __init__(self, value=None):
        self._init_opaque_pointer(value)

    def _init_opaque_pointer(self, value):
        if isinstance(value, COpaquePointer):
            self._as_parameter_ = value._as_parameter_
            return
        if type(self) is COpaquePointer:
            raise TypeError("COpaquePointer must be subclassed")

        self._as_parameter_ = ctypes.c_void_p()
        if value is not None:
            self.move(value)

    def __repr__(self):
        addr = self.get_address()
        if addr == 0:
            return None
        return "<%s: %#x>" % (self.__class__.__name__, addr)

    def get_address(self):
        return self._as_parameter_.
