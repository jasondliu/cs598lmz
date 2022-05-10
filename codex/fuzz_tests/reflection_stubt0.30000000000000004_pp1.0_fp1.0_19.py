fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable

# The __code__ attribute is read-only, so we need to use a descriptor to
# intercept the assignment.

class CodeType(type):
    def __set__(self, instance, value):
        if not isinstance(value, types.CodeType):
            raise TypeError('__code__ must be a code object')
        instance.__dict__['__code__'] = value

class CodeDescriptor(object):
    __metaclass__ = CodeType
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__['__code__']

class FunctionType(type):
    __code__ = CodeDescriptor()

class Function(object):
    __metaclass__ = FunctionType
    def __init__(self, code, globals=None, name=None, argdefs=None,
                 closure=None):
        self.__code__ = code
        self.__name__ = name or
