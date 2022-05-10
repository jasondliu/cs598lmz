import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(f, types.GeneratorType)
# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(abs, types.FunctionType)
assert not isinstance(abs, types.BuiltinMethodType)
assert not isinstance(abs, types.MethodType)
assert not isinstance(abs, types.LambdaType)
assert not isinstance(abs, types.GeneratorType)
# Test types.BuiltinMethodType
assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(abs, types.FunctionType)
assert not isinstance(abs, types.BuiltinMethodType)
assert not isinstance(abs, types.MethodType)
assert not isinstance(
