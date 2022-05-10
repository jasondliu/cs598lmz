import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    __slots__ = ('x',)

def f():
    for x in [1, 2.0, '3', object(), C(), S()]:
        print(type(x), type(x).__dict__)

f()
