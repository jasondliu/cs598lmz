import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    class __metaclass__(type):
        def __new__(self, name, bases, dict):
            d = {}
            for name, value in dict.items():
                if isinstance(value, ctypes.CField):
                    newvalue = property(lambda s, n=name: getattr(s._obj, n).value,
                                        lambda s, n=name, newvalue=value: setattr(s._obj, n, newvalue(newvalue)))
                else:
                    newvalue = value
                d[name] = newvalue
            return super(self, C).__new__(self, name, bases, d)

    def __init__(self, obj):
        self._obj = obj

    def __repr__(self):
        return repr(self._obj)

    __str__ = __repr__

class IP(C):
    # c_ubyte
    ip1 = ctypes.c_ubyte
    ip2 = ctypes.c_ubyte
    ip3 = ctypes.c_ub
