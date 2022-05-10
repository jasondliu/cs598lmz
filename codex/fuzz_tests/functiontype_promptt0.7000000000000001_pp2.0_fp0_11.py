import types
# Test types.FunctionType.
def foo():
    pass
assert isinstance(foo, types.FunctionType)
assert issubclass(types.FunctionType, object)
assert not issubclass(types.FunctionType, type)

# Test types.LambdaType.
foo = lambda x: x
assert isinstance(foo, types.LambdaType)
assert issubclass(types.LambdaType, object)
assert not issubclass(types.LambdaType, type)

# Test types.GeneratorType.
def foo():
    yield 1
gen = foo()
assert isinstance(gen, types.GeneratorType)
assert issubclass(types.GeneratorType, object)
assert not issubclass(types.GeneratorType, type)

# Test types.BuiltinFunctionType.
assert isinstance(range, types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, object)
assert not issubclass(types.BuiltinFunctionType, type)

# Test types.BuiltinMethodType.
assert isinstance(range.__doc__, types.
