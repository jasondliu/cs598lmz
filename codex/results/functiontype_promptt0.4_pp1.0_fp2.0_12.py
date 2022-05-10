import types
# Test types.FunctionType

def foo():
    pass

class bar(object):
    def baz(self):
        pass

assert isinstance(foo, types.FunctionType)
assert not isinstance(bar, types.FunctionType)
assert isinstance(bar.baz, types.FunctionType)

# Test types.LambdaType

assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(foo, types.LambdaType)
assert not isinstance(bar.baz, types.LambdaType)

# Test types.GeneratorType

def foo():
    yield 42

assert isinstance(foo(), types.GeneratorType)
assert not isinstance(foo, types.GeneratorType)
assert not isinstance(bar.baz, types.GeneratorType)

# Test types.MethodType

assert isinstance(bar.baz, types.MethodType)
assert not isinstance(foo, types.MethodType)
assert not isinstance(foo(), types.MethodType)

# Test types.BuiltinFunctionType

assert isinstance
