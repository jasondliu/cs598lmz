import types
# Test types.FunctionType():
def foo(): pass
print(type(foo))
print(type(foo.__init__))
print(isinstance(foo, types.FunctionType))
print(isinstance(foo.__init__, types.FunctionType))

# Test types.LambdaType():
bar = lambda: 0
print(isinstance(bar, types.LambdaType))

# Test types.MethodType():
class A: pass
a = A()
a.foo = foo
print(isinstance(a.foo, types.MethodType))
print(isinstance(a.foo.__init__, types.MethodType))

# Test types.UnboundMethodType():
print(isinstance(A.foo, types.UnboundMethodType))
print(isinstance(A.foo.__init__, types.UnboundMethodType))
