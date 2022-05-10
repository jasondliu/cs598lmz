import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(isinstance, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert isinstance(int, types.TypeType)
assert isinstance(type, types.BuiltinFunctionType)
assert isinstance(range, types.BuiltinFunctionType)
assert isinstance(object, types.TypeType)
assert isinstance(type, types.TypeType)
assert isinstance(object(), types.InstanceType)
assert isinstance(int, types.TypeType)
assert isinstance(types.FunctionType, types.TypeType)

# Test types.LambdaType
f = lambda : None
assert isinstance(f, types.LambdaType)
assert isinstance(f, types.FunctionType)
assert isinstance(lambda : None, types.LambdaType)
assert isinstance(lambda : None, types.FunctionType)

# Test types.GeneratorType
def f():
    yield 1
g = f()
assert isinstance(g, types.Gener
