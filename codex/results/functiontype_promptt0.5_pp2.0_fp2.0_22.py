import types
# Test types.FunctionType
def foo():
    pass
assert isinstance(foo, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
# Test types.GeneratorType
def bar():
    yield 1
assert isinstance(bar(), types.GeneratorType)
