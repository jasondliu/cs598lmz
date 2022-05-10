import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class B(object):
    __slots__ = ('x')

m = types.MappingProxyType({'ctype': ctypes.c_int})

def f():
    print("here")

s = types.SimpleNamespace(x=1)

T = typing.TypeVar("T")

class UntypedType(type):
    def __getitem__(self, types):
        return types

C = UntypedType("C", (object,), {})

def tryfinally_return(x):
    try:
        return x
    finally:
        print("here")
    print("there")
