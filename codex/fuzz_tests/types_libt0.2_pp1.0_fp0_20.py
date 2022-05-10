import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

class A(object):
    pass

a = A()
a.__class__.__name__

a.__class__.__name__ = 'B'
a.__class__.__name__

a.__class__.__name__ = 'C'
a.__class__.__name__

a.__class__.__name__ = 'D'
a.__class__.__name__

a.__class__.__name__ = 'E'
a.__class__.__name__

a.__class__.__name__ = 'F'
a.__class__.__name__

a.__class__.__name__ = 'G'
a.__class__.__name__

a.__class__.__name__ = 'H'
a.__class__.__name__

a.__class__.__name__ = 'I'
a.__class__.__name__

a.__class__.__
