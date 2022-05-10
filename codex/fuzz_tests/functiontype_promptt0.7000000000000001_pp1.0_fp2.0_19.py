import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
f = lambda x: x
assert isinstance(f, types.LambdaType)

# Test types.MethodType
def f():
    pass
assert isinstance(f, types.MethodType)
# Test types.BuiltinFunctionType
# TODO: test with actual builtin functions, not just a lambda
f = lambda x: x
assert isinstance(f, types.BuiltinFunctionType)
