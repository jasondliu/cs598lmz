import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
def h():
    yield 1

assert isinstance(h(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance(g.__code__, types.CodeType)
assert isinstance(h.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except Exception as e:
    assert isinstance(e.__traceback__, types.TracebackType)

# Test types.FrameType
assert isinstance(f.__code__.co_frame, types.FrameType)
assert isinstance(g.__code__.co_frame, types.FrameType)
assert isinstance(h.__code__.co_
