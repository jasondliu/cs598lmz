import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
def h():
    yield 1
    yield 2
g = h()
assert isinstance(g, types.GeneratorType)
assert next(g) == 1
assert next(g) == 2

# Test types.CodeType
def i(): pass
assert isinstance(i.__code__, types.CodeType)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def j():
    return sys._getframe()
assert isinstance(j(), types.FrameType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append
