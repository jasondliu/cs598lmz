import types
# Test types.FunctionType
def foo(): pass
assert isinstance(foo, types.FunctionType)

# Test types.LambdaType
bar = lambda: None
assert isinstance(bar, types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 42
g = gen()
assert isinstance(g, types.GeneratorType)

# Test types.CodeType
assert isinstance(foo.__code__, types.CodeType)
assert isinstance(bar.__code__, types.CodeType)
assert isinstance(gen.__code__, types.CodeType)

# Test types.FrameType
assert isinstance(foo.__code__.co_frame, types.FrameType)
assert isinstance(bar.__code__.co_frame, types.FrameType)
assert isinstance(gen.__code__.co_frame, types.FrameType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType
