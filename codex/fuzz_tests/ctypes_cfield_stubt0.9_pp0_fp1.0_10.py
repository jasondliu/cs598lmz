import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def raiseTypeError(*args):
    raise TypeError
setTypeError = raiseTypeError

def getTypeError():
    return typeError

class InstanceWithCustomTypeError(object):
    __str__ = 'InstaceWithCustomTypeError'

    def __getattribute__(self, attr):
        raise TypeError

class FactoryInstanceWithMethods(object):
    def __getattribute__(self, attr):
        class A(object):
            a = type('A', (object,), {
                '__repr__': lambda self: 'A instance' })
        return object()

class FactoryInstanceWithProperties(object):
    def __getattribute__(self, attr):
        class A(object):
            def __repr__(self): return 'A instance'
            def get_x(self):
                return __builtins__.property(lambda self: 42)
            x = __builtins__.property(lambda self: 42)
        return A()

class Dummy(object):
    def __repr__(self):
        return '
