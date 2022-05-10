import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
g = lambda x: x
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
def h():
    yield 1
    yield 2
    yield 3
assert isinstance(h(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance(g.__code__, types.CodeType)
assert isinstance(h.__code__, types.CodeType)

# Test types.FrameType
def i():
    assert isinstance(sys._getframe(), types.FrameType)
i()

# Test types.TracebackType
try:
    1/0
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.ModuleType
assert isinstance(sys, types.ModuleType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.
