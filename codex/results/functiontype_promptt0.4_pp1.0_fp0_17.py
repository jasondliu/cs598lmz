import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
l = lambda x: x
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g():
    yield
g = g()
assert isinstance(g, types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance(l.__code__, types.CodeType)
assert isinstance(g.gi_code, types.CodeType)

# Test types.FrameType
def h():
    assert isinstance(h.__code__.__frame__, types.FrameType)
h()

# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.BuiltinFunctionType
assert isinstance(len,
