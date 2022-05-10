import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, value):
        self.value = value
    def __ctypes_from_outparam__(self):
        return ctypes.byref(self.value)
    def __ctypes_to_outparam__(self, cls):
        self.value = cls.from_address(ctypes.addressof(self.value))
    def __ctypes_from_param__(self, cls):
        return self.value
    def __ctypes_to_param__(self, cls, value):
        self.value = value

class CField(ctypes.CField):
    def __init__(self, *args, **kwargs):
        if args[2] is not None:
            args = (args[0], args[1], C(args[2]))
        super(CField, self).__init__(*args, **kwargs)

class CStructure(ctypes.Structure):
    _fields_ = [('x', CField('x', ctypes.c_
