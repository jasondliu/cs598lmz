import types
# Test types.FunctionType
def foo(): pass
assert isinstance(foo, types.FunctionType)
assert isinstance(foo, types.BuiltinFunctionType)
assert isinstance(foo, types.BuiltinMethodType)
assert isinstance(foo, types.MethodType)
assert isinstance(foo, types.UnboundMethodType)
assert not isinstance(foo, types.LambdaType)
assert not isinstance(foo, types.GeneratorType)
# Test types.LambdaType
bar = lambda: None
assert isinstance(bar, types.FunctionType)
assert isinstance(bar, types.LambdaType)
assert not isinstance(bar, types.GeneratorType)
# Test types.GeneratorType
def baz(): yield
assert isinstance(baz(), types.GeneratorType)
assert isinstance(baz(), types.GeneratorType)
# Test types.MethodType
class A(object):
    def foo(self): pass
assert isinstance(A.foo, types.MethodType)
assert isinstance(A.foo, types.UnboundMethodType)
assert isinstance(A().
