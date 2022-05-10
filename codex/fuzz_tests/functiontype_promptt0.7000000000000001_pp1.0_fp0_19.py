import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(1, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(1, types.LambdaType)

# Test types.GeneratorType
def g(): yield 1
assert isinstance(g, types.GeneratorType)
assert isinstance(g(), types.GeneratorType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(1, types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert not isinstance(f, types.CodeType)
assert not isinstance(1, types.CodeType)

# Test types.FrameType
assert isinstance(g.__code__, types.FrameType)
assert not isinstance(f, types.FrameType
