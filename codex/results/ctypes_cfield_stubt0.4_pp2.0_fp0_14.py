import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __getattr__(self, name):
        return getattr(self.__dict__['_obj'], name)
    def __init__(self, obj):
        self.__dict__['_obj'] = obj

def test(obj):
    print obj.x
    print type(obj.x)
    print type(obj.x) is ctypes.CField
    print type(obj.x) is CField
    print type(obj.x) is C(S.x)
    print type(obj.x) is C(S.x)._obj
    print type(obj.x) is C(S.x)._obj._type_

test(S(42))
test(C(S(42)))
</code>

