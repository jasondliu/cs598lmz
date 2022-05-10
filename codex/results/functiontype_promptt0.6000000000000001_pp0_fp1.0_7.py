import types
# Test types.FunctionType
def f(): pass
def g(): pass
def h(): pass
f.__name__
g.__name__
h.__name__
f.__name__ = 'foo'
f.__name__
g.__name__ = 'bar'
g.__name__
h.__name__ = 'baz'
h.__name__
# Test types.BuiltinFunctionType
def f(): pass
def g(): pass
def h(): pass
f.__name__
g.__name__
h.__name__
f.__name__ = 'foo'
f.__name__
g.__name__ = 'bar'
g.__name__
h.__name__ = 'baz'
h.__name__
# Test types.MethodType
def f(self): pass
def g(self): pass
def h(self): pass
f.__name__
g.__name__
h.__name__
f.__name__ = 'foo'
f.__name__
g.__name__ = 'bar'
g.__name__
h.__
