import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
g = (x for x in range(10))
assert isinstance(g, types.GeneratorType)

# Test types.CodeType
def f(x):
    return x + 1
assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def f():
    return sys._getframe()

assert isinstance(f(), types.FrameType)

# Test types.GetSetDesc
