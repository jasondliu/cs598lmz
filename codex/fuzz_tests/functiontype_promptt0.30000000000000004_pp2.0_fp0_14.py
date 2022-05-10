import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)

# Test types.LambdaType
f = lambda: None
assert isinstance(f, types.LambdaType)
assert not isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.GeneratorType
def f():
    yield 1

assert isinstance(f(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
assert isinstance(tb.
