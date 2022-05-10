import types
# Test types.FunctionType
# Make sure we can get/set function attributes
def f():
    pass
f.foo = 12
print f.foo
# Test types.LambdaType
# Make sure we can get/set lambda attributes
f = lambda: None
f.foo = 12
print f.foo
# Test types.GeneratorType
# Make sure we can get/set generator attributes
g = (i for i in range(10))
g.foo = 12
print g.foo
# Test types.UnboundMethodType
# Make sure we can get/set method attributes
class A(object):
    pass
A.f = lambda self: None
print A.f.__self__
# Test types.MethodType
# Make sure we can get/set method attributes
class A(object):
    pass
a = A()
a.f = lambda self: None
print a.f.__self__
# Test types.BuiltinFunctionType
# Make sure we can get/set builtin function attributes
print len.__module__
len.foo = 12
print len.foo
# Test types.BuiltinMethodType

