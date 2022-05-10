import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyClass:
    def __init__(self, val):
        self.val = val

    def __getattribute__(self, attr):
        print('__getattribute__ called for %s' % attr)
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):
        print('__getattr__ called for %s' % attr)
        return 'test'

    def __get__(self, obj, type=None):
        print('__get__ called for %s.%s' % (type, self.val))
        return 'test'

class MyClass2(MyClass):
    def __getattribute__(self, attr):
        print('__getattribute__ called for %s' % attr)
        return object.__getattribute__(self, attr)

class MyClass3(MyClass2):
    def __getattribute__(self, attr):
        print('__getattribute__ called for %s' % attr)
        return object.__getattribute__(
