import types
# Test types.FunctionType
def foo(): pass

assert isinstance(foo, types.FunctionType)
assert not isinstance(foo, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)

# Test types.MethodType
class Foo(object):
    def bar(self): pass

assert isinstance(Foo.bar, types.MethodType)
assert not isinstance(Foo.bar, types.FunctionType)

# Test types.UnboundMethodType
assert isinstance(Foo.bar.__func__, types.UnboundMethodType)
assert not isinstance(Foo.bar.__func__, types.MethodType)

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
assert not isinstance((lambda: None), types.FunctionType)

# Test types.GeneratorType
def foo():
    yield None

assert isinstance(foo(), types.GeneratorType)
assert not isinstance(foo(),
