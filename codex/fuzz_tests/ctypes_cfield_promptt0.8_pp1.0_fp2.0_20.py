import ctypes
# Test ctypes.CField() with reference to ctypes.CFUNCTYPE()


class XMeta(type(ctypes.Structure)):
    def __prepare__(self, *args, **kw):
        return collections.OrderedDict()


class X(ctypes.Structure, metaclass=XMeta):
    _fields_ = [
        ('f1', ctypes.CField([ctypes.CFUNCTYPE(ctypes.c_int)])),
    ]


X
