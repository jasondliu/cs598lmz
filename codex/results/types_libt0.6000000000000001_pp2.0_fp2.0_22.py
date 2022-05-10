import types
types.FunctionType

class A(object):
    def __init__(self):
        pass

A.__init__

a = A()

a.__init__

def foo():
    pass

foo.__init__

def bar():
    pass

foo.__init__ = bar.__init__

foo.__init__

foo.__init__ = types.FunctionType(foo.__code__, foo.__globals__, foo.__name__, foo.__defaults__, foo.__closure__)

foo.__init__

foo.__init__ = types.FunctionType(foo.__code__, foo.__globals__, foo.__name__, foo.__defaults__, foo.__closure__)

foo.__init__

foo.__init__ = types.FunctionType(foo.__code__, foo.__globals__, foo.__name__)

foo.__init__

foo.__init__ = types.FunctionType(foo.__code__, foo.__globals
