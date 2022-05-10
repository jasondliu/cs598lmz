import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
f = lambda x: x + 1
assert isinstance(f, types.LambdaType)
assert isinstance(types.LambdaType, types.TypeType)

# Test types.GeneratorType
def gen():
    yield 1
g = gen()
assert isinstance(g, types.GeneratorType)
# Test types.CodeType (not implemented)
# Test types.FrameType (not implemented)
# Test types.TracebackType (not implemented)
# Test types.SliceType (not implemented)
# Test types.ModuleType (not implemented)
# Test types.BuiltinFunctionType (not implemented)
# Test types.BuiltinMethodType (not implemented)
# Test types.DictProxyType (not implemented)

# Test types.MethodType
def f(x):
    return x + 1
assert isinstance(f, types.MethodType)
# TODO: also test types.UnboundMethodType

# Test types.GetSetDescript
